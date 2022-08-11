import gym
import numpy as np
import time
from collections import defaultdict
import sys

class Sarsa():
    def __init__(self):
        self.initial_alpha = 1.0
        self.min_alpha = 0.01
        self.gamma = 1.0
        self.epsilon = 0.05
        self.num_episodes=2000
        self.env = self.load_env()
        self.nA = self.env.action_space.n
        self.Q = defaultdict(lambda : np.zeros([self.nA]))
    def load_env(self):
        env = gym.make('MountainCar-v0')
        low_bounds = env.observation_space.low
        high_bounds = env.observation_space.high
        number_states = 40
        self.POS = np.linspace(low_bounds[0], high_bounds[0], number_states)
        self.VEL = np.linspace(low_bounds[1], high_bounds[1], number_states)
        return env
    def to_bins(self, value, bins):
	    return np.digitize(x=[value], bins=bins)[0]
    def to_state(self, obs):
        p, v = obs
        state = (self.to_bins(p, self.POS), self.to_bins(v, self.VEL))
        return state
    def get_action(self, state):
        if np.random.random() > self.epsilon:
            return np.argmax(self.Q[state])
        else:
            return np.random.choice(self.nA)
    def train(self):
        for i_episode in range(1, self.num_episodes+1):
            if i_episode % 100 == 0:
                print('\rEpisode {}/{}'.format(i_episode, self.num_episodes), end='')
                sys.stdout.flush()
            obs = self.env.reset()
            state = self.to_state(obs)
            alpha = self.initial_alpha-(self.initial_alpha-self.min_alpha)*i_episode/self.num_episodes
            while True:
                action = self.get_action(state)
                next_obs, reward, done, info = self.env.step(action)
                next_state = self.to_state(next_obs)
                next_action = self.get_action(next_state)
                self.Q[state][action] += alpha*(reward + self.gamma*self.Q[next_state][next_action] - self.Q[state][action])
                if done:
                    break
                state = next_state
    def run(self, render=False):
        total_reward = 0
        obs = self.env.reset()
        state = self.to_state(obs)
        while True:
            action = self.get_action(state)
            next_obs, reward, done, info = self.env.step(action)
            next_state = self.to_state(next_obs)
            total_reward += reward
            if render:
                self.env.render()
            if done:
                print(total_reward)
                break
            state = next_state


agent = Sarsa()
agent.train()
agent.run(render=True)