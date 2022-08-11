import gym
import time
import numpy as np
import sys

def hill_climbing(env):
    episodes = 10000
    best_reward = 0
    best_W = np.array([-0.54582786, 0.99685559, 0.83120262, 1.03384631])
    best_b = np.array([0.42914615])
    for i_episode in range(episodes):
        if i_episode % 100 == 0:
            print('\rEpisode {}/{}'.format(i_episode, episodes), end='')
            sys.stdout.flush()
        state = env.reset()
        total_reward = 0
        W = best_W
        b = best_b
        while True:
            action = 1 if np.dot(W, state) + b >= 0 else 0
            next_state, reward, done, info = env.step(action)
            total_reward += reward
            if done:
                if total_reward >= best_reward:           
                    best_reward = total_reward
                    best_W = W + np.random.normal(0, 0.1, env.observation_space.shape[0])
                    best_b = b + np.random.normal(0, 0.1, 1)
                    print(total_reward, end='')
                    print(best_W, end='')
                    print(best_b)
                break
            state = next_state
    return best_W, best_b
def run(env, W, b):
    state = env.reset()
    total_reward = 0
    while True:
        action = 1 if np.dot(W, state) + b >= 0 else 0
        next_state, reward, done, info = env.step(action)
        total_reward += reward
        # if not done:
        #     time.sleep(1)
        #     env.render()
        if done:
            print(total_reward)
            break
        state = next_state


env = gym.make('CartPole-v0')
best_W, best_b = hill_climbing(env)
run(env, best_W, best_b)
env.close()