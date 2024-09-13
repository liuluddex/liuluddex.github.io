import os
import sys
import json
import gymnasium as gym
from gymnasium import spaces
import numpy as np
from copy import deepcopy
from typing import Optional, Any

from gymnasium.core import ObsType
from scipy.optimize import minimize
import pygame

from tools.logs import Logger
from adas_env.utils import ellipse_distance, objective, constraint, ReachableSet


class ADASEnv(gym.Env):
  """
  攻击dr的一维状态下的表现
  """

  def __init__(self, verbose=False, env_config='S1-dr'):
    super(ADASEnv, self).__init__()

    # 导入当前env的初始状态
    # class_name = self.__class__.__name__
    self.env_config = env_config
    class_name = env_config
    config_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'envs')
    configs = json.load(open(os.path.join(config_path, f'{class_name}.json')))
    self._init_state = configs['init_state']
    self.sim_step = configs['sim_step']
    self.sim_time = configs['sim_time']
    self._atk_param = configs['attack_parameter']

    # 导入当前env存在的不安全集合
    unsafe_set_path = os.path.join(os.path.dirname(__file__), '..', 'configs', 'unsafe_sets', f'{class_name}.json')
    self._unsafe_set = ReachableSet([], [], set_file_path=unsafe_set_path)

    # 根据当前的不安全集合求得拟合的椭圆
    params = self.get_ellipse_params()
    self._center = params[0]
    self._semi_major = params[1]
    self._semi_minor = params[2]
    self._theta = params[3]

    # 计算出强化学习所需的初始状态
    self._init_state = self._init_state + [self._init_state[self._atk_param]]
    distance = ellipse_distance([self._init_state[0], self._init_state[8]], self._center,
                                self._semi_major, self._semi_minor, self._theta)
    self._init_state += [self._center[0], self._center[1], self._semi_major, self._semi_minor, distance]
    self._init_state = np.array(self._init_state, dtype=np.float32)
    self._state = deepcopy(self._init_state)

    # 动作空间和状态空间
    self.action_space = spaces.Discrete(configs['num_actions'])
    self.action_low = configs['action_low']
    self.action_high = configs['action_high']
    self.action_coefficient = (self.action_high - self.action_low) / (self.action_space.n - 1)
    self.observation_space = spaces.Box(low=-1e9, high=1e9, shape=self._init_state.shape, dtype=np.float32)

    # 其他配置项
    self.cur_time = 0.0
    self.q = configs['q']
    self.c = configs['c']
    self.d0 = configs['d0']
    self.histories = []
    self.history_actions = []
    self.total_cost = 0.0
    self.noise_weight = configs['noise_weight']
    self.max_cost = configs['max_cost']
    self.num_episodes = 0
    self.min_cost = 1e9
    self.num_success = 0
    self.avg_cost = 0.0

    # Agent动作可视化的配置
    self.verbose = verbose

    if self.verbose:
      # initial parameters of pygame
      pygame.init()
      self._WIDTH, self._HEIGHT = 1200, 400
      self._screen = pygame.display.set_mode((self._WIDTH, self._HEIGHT))
      pygame.display.set_caption(f'Scenario of {class_name.replace("_", "-")}')
      self.font = pygame.font.SysFont('Arial', 18)

      # define colors
      self._WHITE = (255, 255, 255)
      self._GRAY = (200, 200, 200)
      self._RED = (255, 0, 0)
      self._BLUE = (0, 0, 255)

      # define parameters of lanes and cars
      self._lane_y = self._HEIGHT // 2 - 50  # 车道在屏幕中的y位置
      self._lane_height = 100  # 车道高度

      self.car_width, self.car_height = 90, 90  # 车辆的宽和高
      self.car1_x, self.car1_y = 100, self._lane_y + 5  # 第一个车的初始位置
      self.car2_x, self.car2_y = self.car1_x + self._state[8] / 4 * self.car_height, self._lane_y + 5  # 第二个车的初始位置

      # load images of cars
      static_path = os.path.join(os.path.dirname(__file__), '..', 'static')
      self.car1_image = pygame.transform.scale(pygame.image.load(os.path.join(static_path, 'car.jpg')),
                                               (self.car_width, self.car_height))
      self.car1_image = pygame.transform.rotate(self.car1_image, -90)

      self.car2_image = pygame.transform.scale(pygame.image.load(os.path.join(static_path, 'car.jpg')),
                                               (self.car_width, self.car_height))
      self.car2_image = pygame.transform.rotate(self.car2_image, -90)

      self._clock = pygame.time.Clock()
      self._tick = 120

  def is_action_valid(self, action: int):
    if self.total_cost + np.abs(self.action_coefficient * action) * self.sim_step >= self.max_cost:
      # print('1')
      return False

    if self.env_config[:2] == 'S1' and self.q != 3 and action != 0:
      # print('2')
      return False

    if self.env_config[:2] == 'S2' and self.q != 3 and action != 0:
      # print('3')
      return False

    return True

  def reset(self, *, seed: Optional[int] = None, options: Optional[dict] = None):
    super().reset(seed=seed)

    self.cur_time = 0.0
    self._state = deepcopy(self._init_state)
    self.q = 1
    self.total_cost = 0.0
    self.history_actions.clear()
    self.histories.clear()
    self.transfer()

    return self._state, {}

  def get_state(self):
    return self._state

  def get_states(self):
    # q, t, a1, v1, d1, a2, v2, d2, vr, dr, dr_atk / v1_atk
    keys = ['q', 't', 'a1', 'v1', 'd1', 'a2', 'v2', 'd2', 'vr', 'dr', 'dr_atk' if self._atk_param == 8 else 'v1_atk']
    items = {key: [] for key in keys}
    for i, key in enumerate(keys):
      values = [history[i] for history in self.histories]
      items[key] = values
    return items

  def step(self, action: int):
    """
    env的核心函数，传入动作，传出agent执行动作后的环境反馈
    Args:
        action:

    Returns:

    """
    # self.history_actions.append(action)

    if not self.is_action_valid(action):
      action = 0

    self.transfer()
    self.update(action)
    # self.histories.append([self.q] + self._state[:10].tolist())
    return self.get_feedback()

  def get_feedback(self):
    d, dr = self._state[14], self._state[8]
    if d > 1:
      reward_ellipse = np.exp(-np.sqrt(d - 1))
    else:
      reward_ellipse = 1.0

    if dr > 3:
      reward_target = np.exp(-np.sqrt(dr - 3))
    else:
      reward_target = 1.0

    reward_cost = (1 - self.total_cost / self.max_cost) * self.noise_weight

    reward = reward_ellipse + reward_target + reward_cost

    t, a1, v1, d1, a2, v2, d2, vr, dr, param = self._state[:10]

    if self.q == 0:
      terminated = True
      info = {'status': 'failed', 'total_cost': self.total_cost}
    elif self.q == 4 and v1 < v2:
      terminated = True
      # print('1')
      info = {'status': 'failed', 'total_cost': self.total_cost}
    elif d > 1:
      if self.q == 0:
        terminated = True
        # print('2')
        info = {'status': 'failed', 'total_cost': self.total_cost}
      else:
        if self.total_cost > self.max_cost:
          terminated = True
          # print('3')
          info = {'status': 'cost limit', 'total_cost': self.total_cost}
        elif self.sim_time - self.cur_time <= 0:
          terminated = True
          # print('4')
          info = {'status': 'failed', 'total_cost': self.total_cost}
        else:
          terminated = False
          info = {'status': 'not terminated', 'total_cost': self.total_cost}
    else:
      if self.total_cost > self.max_cost:
        terminated = True
        # print('5')
        info = {'status': 'cost limit', 'total_cost': self.total_cost}
      elif (t, dr) in self._unsafe_set:
        terminated = True
        # print('6')
        info = {'status': 'success', 'total_cost': self.total_cost}
      else:
        terminated = False
        info = {'status': 'not terminated', 'total_cost': self.total_cost}

    if terminated:
      self.num_episodes += 1

      if info['status'] == 'success':
        self.min_cost = min(self.min_cost, self.total_cost)
        if self.total_cost <= self.max_cost:
          self.avg_cost = self.avg_cost * self.num_success + self.total_cost
          self.num_success += 1
          self.avg_cost /= self.num_success

    if self.verbose:
      self.car1_x = (self._state[3] - self._init_state[3]) / 4 * self.car_height + 100
      self.car2_x = self.car1_x + self._state[8] / 4 * self.car_height + self.car_height

    return self._state, reward, terminated, False, info

  def update(self, action):
    """
    用以更新状态的
    Returns:

    """
    self.cur_time += self.sim_step

    # 更新a1
    self.update_a1()
    # 更新状态
    self.update_state()
    # 模拟攻击过程
    self.attack_simulate(action)
    # 更新到椭圆圆心的距离
    self.update_distance()

  def transfer(self):
    t, a1, v1, d1, a2, v2, d2, vr, dr, param = self._state[:10]

    if self._atk_param == 8:
      dr_atk = param

      if self.q == 1:
        if dr_atk >= 75 and dr >= 0:
          self.q = 1
        elif v2 <= v1 and -(dr_atk - 3) - 1.6 * (v2 - v1) >= 0 and 3 <= dr_atk <= 75 and dr >= 0:
          self.q = 3
        elif v2 <= v1 and -(dr_atk - 3) - 1.6 * (v2 - v1) <= 0 and 3 <= dr_atk <= 75 and dr >= 0:
          self.q = 2
        else:
          self.q = 0
      elif self.q == 2:
        if v2 <= v1 and -(dr_atk - 3) - 1.6 * (v2 - v1) <= 0 and 3 <= dr_atk <= 75 and dr >= 0:
          self.q = 2
        elif v2 <= v1 and -(dr_atk - 3) - 1.6 * (v2 - v1) >= 0 and 3 <= dr_atk <= 75 and dr >= 0:
          self.q = 3
        else:
          self.q = 0
      elif self.q == 3:
        if v2 <= v1 and -(dr_atk - 3) - 1.6 * (v2 - v1) >= 0 and -(dr_atk - 3) - 0.6 * (
          v2 - v1) <= 0 and dr_atk >= 3 and dr >= 0:
          self.q = 3
        elif v2 <= v1 and -(dr_atk - 3) - 1.6 * (v2 - v1) <= 0 and 3 <= dr_atk <= 75 and dr >= 0:
          self.q = 2
        elif v1 >= 0 and -(dr_atk - 3) - 0.6 * (v2 - v1) >= 0 and 3 <= dr_atk <= 75 and dr >= 0:
          self.q = 4
        else:
          self.q = 0
      elif self.q == 4:
        if v1 >= 0 and dr_atk >= 3 and dr >= 0:
          self.q = 4
        elif dr <= 0:
          self.q = 0
        else:
          self.q = 4
      else:
        self.q = 0
    else:
      v1_atk = param
      if self.q == 1:
        if v1_atk <= v2:
          self.q = 1
        elif dr >= 75 and dr >= 0:
          self.q = 1
        elif v2 <= v1_atk and -(dr - 3) - 1.6 * (v2 - v1_atk) >= 0 and 3 <= dr <= 75 and dr >= 0:
          self.q = 3
        elif v2 <= v1_atk and -(dr - 3) - 1.6 * (v2 - v1_atk) <= 0 and 3 <= dr <= 75 and dr >= 0:
          self.q = 2
        else:
          self.q = 0
      elif self.q == 2:
        if v2 <= v1_atk and -(dr - 3) - 1.6 * (v2 - v1_atk) <= 0 and 3 <= dr <= 75 and dr >= 0:
          self.q = 2
        elif v2 <= v1_atk and -(dr - 3) - 1.6 * (v2 - v1_atk) >= 0 and 3 <= dr <= 75 and dr >= 0:
          self.q = 3
        elif v2 >= v1_atk:  # only for S2-v1
          self.q = 1
        else:
          self.q = 0
      elif self.q == 3:
        if v2 <= v1_atk and -(dr - 3) - 1.6 * (v2 - v1_atk) >= 0 and -(dr - 3) - 0.6 * (
          v2 - v1_atk) <= 0 and dr >= 3 and dr >= 0:
          self.q = 3
        elif v2 <= v1_atk and -(dr - 3) - 1.6 * (v2 - v1_atk) <= 0 and 3 <= dr <= 75 and dr >= 0:
          self.q = 2
        elif v1_atk >= 0 and -(dr - 3) - 0.6 * (v2 - v1_atk) >= 0 and 3 <= dr <= 75 and dr >= 0:
          self.q = 4
        else:
          self.q = 0
      elif self.q == 4:
        if v1_atk >= 0 and dr >= 3 and dr >= 0:
          self.q = 4
        elif dr <= 0:
          self.q = 0
        else:
          self.q = 4
      else:
        self.q = 0

  def update_distance(self):
    d = ellipse_distance([self._state[0], self._state[8]], self._center,
                         self._semi_major, self._semi_minor, self._theta)
    self._state[14] = d

  def partial_derivative(self, _state):
    t, a1, v1, d1, a2, v2, d2, vr, dr, atk_param = _state
    if v1 < 0:
      v1 = 0
      a1 = 0

    return np.array([
      1,
      0,
      a1,
      v1,
      0,
      a2,
      v2,
      0,
      v2 - v1,
      v2 - v1 if self._atk_param == 8 else a1  # 判断攻击的是dr还是v1
    ])

  def update_state(self):
    # 更新状态
    k1 = self.partial_derivative(self._state[:10])
    k2 = self.partial_derivative(self._state[:10] + 0.5 * self.sim_step * k1)
    k3 = self.partial_derivative(self._state[:10] + 0.5 * self.sim_step * k2)
    k4 = self.partial_derivative(self._state[:10] + self.sim_step * k3)
    self._state[:10] = self._state[:10] + (self.sim_step / 6.0) * (k1 + 2 * k2 + 2 * k3 + k4)

    t, a1, v1, d1, a2, v2, d2, vr, dr, param = self._state[:10]
    v1 = max(v1, 0)
    vr = v2 - v1
    self._state[2] = v1
    self._state[7] = vr

  def attack_simulate(self, action):
    # print(f'action {self.action_coefficient * action:.4f}')
    self._state[9] += self.action_coefficient * action * self.sim_step
    self.total_cost += np.abs(self.action_coefficient * action) * self.sim_step

  def update_a1(self):
    if self.q == 1:
      a1 = 0
    elif self.q == 2:
      if self._atk_param == 8:
        a1 = self.c * (self.d0 - self._state[9]) * self._state[7]
      else:
        a1 = self.c * (self.d0 - self._state[8]) * self._state[7]
    elif self.q == 3:
      a1 = -4.9
    else:
      a1 = -9.8
    self._state[1] = a1

  def get_ellipse_params(self):
    points = np.array(self._unsafe_set.get_bound_points())
    centroid = np.mean(points, axis=0)
    initial_params = np.array([2, 1, centroid[0], centroid[1], 0])

    cons = {'type': 'ineq', 'fun': lambda params: constraint(points, params)}
    result = minimize(objective, initial_params, constraints=cons, method='SLSQP', options={'disp': False})

    optimal_params = result.x
    _center = [optimal_params[2], optimal_params[3]]
    _semi_major = optimal_params[0]
    _semi_minor = optimal_params[1]
    ang = optimal_params[4] / np.arccos(-1) * 180
    ang = ang % 180
    _theta = ang / 180 * np.arccos(-1)

    return _center, _semi_major, _semi_minor, _theta
