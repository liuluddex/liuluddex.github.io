import os
import sys
import json
import time
import random
import warnings

import numpy as np
from tqdm import tqdm
from copy import deepcopy
import gymnasium as gym

sys.path.append('.')

import adas_env
from tools.logs import Logger
from tools.utils import choose_action, cross_entropy_method


warnings.filterwarnings('ignore')


class RandAgent:
    def __init__(self, env_config='S1-dr'):
        super(RandAgent, self).__init__()

        self.env = gym.make('ADAS', env_config=env_config)
        self.env.reset()

    def explore(self, num_steps=1000000):
        assert hasattr(self.env, 'sim_time'), 'env has no attribute sim_time'
        assert hasattr(self.env, 'sim_step'), 'env has no attribute sim_step'
        assert hasattr(self.env, 'max_cost'), 'env has no attribute max_cost'
        assert hasattr(self.env, 'action_space'), 'env has no attribute action_space'
        assert hasattr(self.env, 'action_low'), 'env has no attribute action_low'
        assert hasattr(self.env, 'action_high'), 'env has no attribute action_high'

        sim_time = getattr(self.env, 'sim_time')
        sim_step = getattr(self.env, 'sim_step')
        max_cost = getattr(self.env, 'max_cost')
        num_actions = getattr(getattr(self.env, 'action_space'), 'n')
        action_range = abs(getattr(self.env, 'action_low') - getattr(self.env, 'action_high'))
        cost_step = action_range / (num_actions - 1) * sim_step

        start = time.time()

        min_cost = 1e9
        avg_cost = 0.0
        num_success = 0
        num_episodes = 0

        observation, info = self.env.reset()

        for _ in tqdm(range(num_steps)):
            action = self.env.action_space.sample()
            if not self.env.is_action_valid(action):
                action = 0

            observation, reward, terminated, truncated, info = self.env.step(action)

            if terminated or truncated:
                num_episodes += 1

                if info['status'] == 'success':
                    avg_cost += self.env.total_cost
                    min_cost = min(min_cost, self.env.total_cost)
                    num_success += 1

                if num_success != 0:
                    Logger.debug(
                        f'num episodes {num_episodes}, average cost {avg_cost / num_success:.3f}, minimum cost {min_cost:.3f}, successful rate {num_success / num_episodes * 100:.3f}%, total cost {self.env.total_cost:.3f}')
                else:
                    Logger.debug(
                        f'num episodes {num_episodes}, average cost {0.0:.3f}, minimum cost {min_cost:.3f}, successful rate {num_success / num_episodes * 100:.3f}%, total cost {self.env.total_cost:.3f}')

                observation, info = self.env.reset()

        end = time.time()
        avg_cost /= num_success
        Logger.info(f'avg cost {avg_cost:.3f}, min cost {min_cost:.3f}, time cost {end - start:.3f}s, successful rate {num_success / num_episodes * 100:.3f}%')


if __name__ == '__main__':
    agent = RandAgent(env_config='S2-v1')
    agent.explore(10000000)
