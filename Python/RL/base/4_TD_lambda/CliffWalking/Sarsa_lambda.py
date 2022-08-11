import gym
import numpy as np
import time
from collections import defaultdict
import sys

class Sarsa_lambda():
    def __init__(self, epsilon=0.1, alpha=1.0, gamma=0.8, _lambda=0.9, episodes=1000):
        self.epsilon = episodes
        self.alpha = alpha
        self.gamma = gamma
        self._lambda = _lambda      # _lambda--迹退化参数
        self.episodes = episodes
        self.env = self.load_env()
        self.nS = self.env.observation_space.n
        self.nA = self.env.action_space.n
        self.Q = defaultdict(lambda : np.zeros(self.nA))
        self.policy = self.make_random_policy(self.nA)
    def load_env(self):
        env = gym.make('CliffWalking-v0')
        # env = gym.make('FrozenLake-v1')
        return env

    def make_random_policy(self, nA):
        def policy_fn(observation):
            A = np.random.choice(np.arange(nA))
            return A
        return policy_fn

    def make_epsilon_greedy_policy(self, Q, epsilon, nA):
        def policy_fn(observation):
            if np.random.random() > epsilon:
                return np.argmax(Q[observation])
            else:
                return np.random.choice(np.arange(nA))
        return policy_fn

    def train(self):
        start = time.time()
        self.policy = self.make_epsilon_greedy_policy(self.Q, self.epsilon, self.nA)    
        for i_episode in range(1, self.episodes+1):
            if i_episode % 100 == 0:
                print('\rEpisode {}/{}'.format(i_episode, self.episodes), end='')
                sys.stdout.flush()
            total_reward = 0
            state = self.env.reset()
            # Eligibility--资格迹
            E = defaultdict(lambda : np.zeros(self.nA))
            while True:
                # epsilon-greedy-policy, 采样
                action = self.policy(state)
                next_state, reward, done, info = self.env.step(action)
                total_reward += reward
                # epsilon-greedy-policy, 更新
                next_action = self.policy(next_state)
                delta = reward + self.gamma * self.Q[next_state][next_action] - self.Q[state][action]
                # print(delta)
                E[state][action] += 1
                for state in range(self.nS):
                    for action in range(self.nA):
                        self.Q[state][action] += self.alpha * delta * E[state][action]
                        E[state][action] = self.gamma * self._lambda * E[state][action]
                if done:
                    break
                state = next_state
        print('消耗时间：{}'.format(time.time()-start))
    def run_game(self, render=False):
        start = time.time()
        state = self.env.reset()
        total_reward = 0
        while True:
            action = self.policy(state)
            next_state, reward, done, info = self.env.step(action)
            total_reward += reward 
            if render:
                self.env.render()
            if done:
                break
            state = next_state
        print('消耗时间：{}'.format(time.time()-start))

if __name__ == '__main__':
    s = Sarsa_lambda()
    s.train()
    s.run_game(render=True)
