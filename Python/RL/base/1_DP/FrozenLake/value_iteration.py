import gym
import time
import numpy as np

def value_iteration(env, threshold=1e-4, gamma=1.0):
    env.reset()
    start = time.time()
    policy = np.zeros(env.nS, dtype=int)
    value_table = np.zeros(env.nS)
    new_value_table = np.zeros(env.nS)
    delta = 2*threshold
    while delta > threshold:
        for state in range(env.nS):
            action_value = np.zeros(env.nA)
            for action in range(env.nA):
                for prob, next_state, reward, done in env.P[state][action]:
                    action_value[action] += prob*(reward+gamma*value_table[next_state])
            new_value_table[state] = max(action_value)
            policy[state] = np.argmax(action_value)
        delta = sum(np.fabs(new_value_table-value_table))
        value_table = np.copy(new_value_table)
    end = time.time()
    print('消耗时间：{}'.format(end-start))
    return value_table, policy

def play_game(env, policy, episodes=1, timesteps=150):
    for episode in range(episodes):
        state = env.reset()
        for t in range(timesteps):
            action = policy[state]
            state, reward, done, info = env.step(action)
            env.render()
            time.sleep(1)
            if done:
                break

if __name__ == '__main__':
    env = gym.make('FrozenLake-v1')
    value_table, policy = value_iteration(env, gamma=1.0)
    print(value_table.reshape(4,4))
    time.sleep(10)
    play_game(env, policy)
    env.close()