import gym
from gym import envs
import numpy as np
import time
import sys
from collections import defaultdict

np.random.seed(2)

def make_random_policy(nA):
    def policy_fn(observation):
        A = np.ones(nA)/nA
        return A
    return policy_fn

def make_epsilon_greedy_policy(Q, epsilon, nA):
    def policy_fn(observation):
        A = np.ones(nA, dtype=float)*epsilon/nA
        best_action = np.argmax(Q[observation])
        A[best_action] += (1.0-epsilon)
        return A
    return policy_fn

def mc_control_greedy_policy(env, num_episodes, discount_factor=1.0, epsilon=0.1):
    returns_sum = defaultdict(float)
    returns_count = defaultdict(float)
    Q = defaultdict(lambda : np.zeros(env.action_space.n))
    policy = make_epsilon_greedy_policy(Q, epsilon, env.action_space.n)
    for i_episode in range(1, num_episodes+1):
        if i_episode % 1000 == 0:
            print('\rEpisode{}/{}'.format(i_episode, num_episodes))
            sys.stdout.flush()
        episode = []
        state = env.reset()
        for t in range(100):
            probs = policy(state)
            action = np.random.choice(np.arange(len(probs)), p=probs)
            next_state, reward, done, _ = env.step(action)
            episode.append((state, action, reward))
            if done:
                break
            state = next_state
        sa_in_episode = set([(tuple(x[0]), x[1]) for x in episode])
        for state, action in sa_in_episode:
            sa_pair = (state, action)
            first_occurence_idx = next(i for i, x in enumerate(episode) if x[0]==state and x[1]==action)
            G = sum([x[2]*(discount_factor**i) for i,x in enumerate(episode[first_occurence_idx:])])
            returns_sum[sa_pair] += G
            returns_count[sa_pair] += 1.0
            Q[state][action] = returns_sum[sa_pair]/returns_count[sa_pair]
    return Q, policy

def run_game(env, policy, episodes):
    wins = 0
    for i_episode in range(episodes):
        state = env.reset()
        probs = policy(state)
        while True:
            action = np.random.choice(np.arange(len(probs)), p=probs)
            state, reward, done, info = env.step(action)
            if done:
                # print('Reward:',reward)
                # print('You win\n') if reward > 0 else print('You lose')
                wins += 1 if reward > 0 else 0
                break
    win_ratio = wins/episodes
    print(win_ratio)

if __name__ == '__main__':
    # print('\n'.join([env_spec.id for env_spec in envs.registry.all()]))

    env = gym.make('Blackjack-v0')

    # 随机策略
    # policy = make_random_policy(env.action_space.n)
    # run_game(env, policy=policy, episodes=500)

    # 在线蒙特卡罗
    Q, policy = mc_control_greedy_policy(env, num_episodes=50000, epsilon=0.01)
    run_game(env, policy=policy, episodes=500)
    
    env.close()
    