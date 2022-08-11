# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()
import gym
import numpy as np
import time
import sys
from collections import defaultdict

class Sarsa_Increment():
    def __init__(self, alpha=1.0, gamma=1.0, epsilon=0.01, episodes=1000):
        self.alpha = alpha
        self.gamma = gamma
        self.epsilon = epsilon
        self.episodes = episodes
        self.env = self.load_env()
        self.nA = self.env.action_space.n
        self.Q = defaultdict(lambda : np.zeros(self.nA))
        self.policy = self.make_random_choice(self.nA)
        self.theta = np.zeros(2+1)
    def load_env(self):
        env = gym.make('MountainCar-v0')
        return env
    def make_random_choice(self, nA):
        def policy_fn(observation):
            A = np.random.choice(np.arange(nA))
            return A
        return policy_fn
    def make_epsilon_random_choice(self, Q, epsilon, nA):
        def policy_fn(observation):
            if np.random.random() > epsilon:
                return np.argmax(Q[observation])
            else:
                return np.random.choice(np.arange(nA))
        return policy_fn
    def x(self, state, action):
        return np.append(state, action)
    def train(self):
        self.policy = self.make_epsilon_random_choice(self.Q, self.epsilon, self.nA)
        for i_episode in range(1, self.episodes+1):
            if i_episode % 100 == 0:
                print('\rEpisode {}/{}'.format(i_episode, self.episodes), end='')
                sys.stdout.flush()
            total_reward = 0
            state = self.env.reset()
            while True:
                action = self.policy((state[0], state[1]))
                next_state, reward, done, info = self.env.step(action)
                total_reward += reward
                next_action = self.policy((next_state[0], next_state[1]))
                self.theta = self.theta - self.alpha * (reward + self.gamma * np.dot(self.theta, self.x(next_state, next_action)) - np.dot(self.theta, self.x(state, action))) * self.x(state, action)
                self.Q[(state[0], state[1])][action] = np.dot(self.theta, self.x(state, action)) 
                if not done:
                    self.env.render()
                    print(self.theta, end='')
                    print(self.Q[(state[0], state[1])], end='')
                    print(self.policy((state[0], state[1])))
                if done:
                    break
                state = next_state
    def run_game(self, render=False):
        state = self.env.reset()
        total_reward = 0
        while True:
            action = self.policy((state[0], state[1]))
            next_state, reward, done, info = self.env.step(action)
            total_reward += reward 
            if render:
                self.env.render()
            if done:
                break
            state = next_state
    

if __name__ == '__main__':
    model = Sarsa_Increment()
    model.train()
    model.run_game(render=True)
        