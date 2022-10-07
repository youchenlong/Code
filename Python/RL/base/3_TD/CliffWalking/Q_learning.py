import gym
import numpy as np
import random
from collections import defaultdict
import time
import sys

class Q_learning():
    def __init__(self, epsilon=0.1, alpha=0.01, gamma=1.0, episodes=3000):
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.episodes = episodes
        self.env = self.load_env()
        self.nA = self.env.action_space.n
        self.Q = defaultdict(lambda : np.zeros(self.nA))
        self.policy = self.make_random_policy(self.nA)
    def load_env(self):
        env = gym.make('CliffWalking-v0')
        # env = gym.make('Blackjack-v1')
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
            while True:
                # epsilon-greedy-policy, 采样
                action = self.policy(state)
                next_state, reward, done, info = self.env.step(action)
                total_reward += reward
                # greedy-policy, 更新
                next_action = np.argmax(self.Q[next_state])
                self.Q[state][action] += self.alpha * (reward + self.gamma * self.Q[next_state][next_action] - self.Q[state][action])
                if done:
                    break
                state = next_state
        print('消耗时间：{}', time.time()-start)

    def run_game(self, render=False):
        state = self.env.reset()
        total_reward = 0
        while True:
            action = self.policy(state)
            next_state, reward, done, info = self.env.step(action)
            total_reward += reward 
            if render:
                self.env.render()
                time.sleep(0.2)
            if done:
                break
            state = next_state

if __name__ == '__main__':
    model = Q_learning()
    model.train()
    model.run_game(render=True)