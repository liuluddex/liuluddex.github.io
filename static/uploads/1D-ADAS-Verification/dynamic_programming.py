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


class DPAgent:
    def __init__(self, env_config='S1-dr'):
        super(DPAgent, self).__init__()

        self.env = gym.make('ADAS', env_config=env_config)
        self.env.reset()

    def explore(self, num_steps=500000):
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

        num_sim_steps = int(sim_time / sim_step + 0.5) + 1
        num_cost_steps = int(max_cost / cost_step + 0.5) + 1

        dp = [None for _ in range(num_cost_steps)]
        env = deepcopy(self.env)
        dp[0] = env

        start = time.time()

        min_cost = 1e9
        avg_cost = 0.0
        num_success = 0

        best_actions = None
        for i in tqdm(range(num_sim_steps)):
            new_dp = dp[:]
            for j in range(num_cost_steps - 1, -1, -1):
                if dp[j] is not None and dp[j].get_state()[8] < 3:
                    continue

                for k in range(num_actions):
                    if j >= k and dp[j - k] is not None and dp[j - k].total_cost != 1e9:
                        new_env = deepcopy(dp[j - k])
                        new_env.step(action=k)
                        if new_dp[j] is None or new_env.get_state()[8] < new_dp[j].get_state()[8]:
                            new_dp[j] = new_env
            dp = new_dp

            for j in range(num_cost_steps):
                if dp[j] is not None and dp[j].get_state()[8] < 3:
                    # if min_cost > dp[j].total_cost:
                    #     best_actions = dp[j].history_actions

                    min_cost = min(min_cost, dp[j].total_cost)
                    avg_cost += dp[j].total_cost
                    num_success += 1

        avg_cost /= num_success

        end = time.time()
        Logger.info(f'min cost {min_cost:.3f}, avg cost {avg_cost:.3f}, time cost {end - start:.3f}s')
        # Logger.info(f'best actions {best_actions}')

        # best_actions = np.array(best_actions, dtype=np.int32)
        # np.save(f'{env.__str__()}_best_actions.npy', best_actions, allow_pickle=True)


if __name__ == '__main__':
    agent = DPAgent(env_config='S2-dr')
    agent.explore()
