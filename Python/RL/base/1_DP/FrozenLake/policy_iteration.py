import gym
from gym import envs
import time
import numpy as np

np.random.seed(2)

def policy_evaluation(env, value_table, policy, discount_factor=1.0, threshold=1e-4):
    delta = 2*threshold
    while delta > threshold:
        new_value_table = np.zeros(env.nS)
        for state in range(env.nS):
            action = policy[state]
            for prob, next_state, reward, done in env.P[state][action]:
                new_value_table[state] += prob*(reward+discount_factor*value_table[next_state])
        delta = sum(np.fabs(new_value_table - value_table))
        value_table = new_value_table
    return value_table

def policy_improvement(env, value_table, policy, discount_factor=1.0):
    while True:
        old_policy = np.copy(policy)
        for state in range(env.nS):
            action_value = np.zeros(env.nA)
            for action in range(env.nA):
                for prob, next_state, reward, done in env.P[state][action]:
                    action_value[action] += prob*(reward+discount_factor*value_table[next_state])
            policy[state] = np.argmax(action_value)
        if np.all(policy==old_policy):
            break
    return policy

def policy_iteration(env, iterations, discount_factor=1.0):
    env.reset()
    start = time.time()
    policy = np.random.randint(low=0, high=env.nA, size=env.nS)
    value_table = np.zeros(env.nS)
    for step in range(iterations):
        old_policy = np.copy(policy)
        value_table = policy_evaluation(env, value_table, policy, discount_factor)
        policy = policy_improvement(env, value_table, policy, discount_factor)
        if np.all(policy==old_policy):
            end = time.time()
            print('消耗时间：{}'.format(end-start))
            break
    return value_table, policy

def play_game(env, policy, episodes=1, timesteps=150):
    for episode in range(episodes):
        state = env.reset()
        for t in range(timesteps):
            action = policy[state]
            state, reward, done, info = env.step(action)
            env.render()
            time.sleep(0.1)
            if done:
                break

if __name__ == '__main__':
    # print('\n'.join([env_spec.id for env_spec in envs.registry.all()]))

    env = gym.make('FrozenLake-v0')
    value_table, policy = policy_iteration(env, iterations=6, discount_factor=1.0)
    print(value_table.reshape(4,4))
    play_game(env, policy)
    env.close()