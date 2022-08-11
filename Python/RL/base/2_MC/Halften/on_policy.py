# import gym
# import matplotlib
import numpy as np
import sys
from collections import defaultdict
# from HalftenEnv import HalftenEnv
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
# from matplotlib.ticker import MultipleLocator, FormatStrFormatter

def make_epsilon_greedy_policy(Q, epsilon, nA):
    def policy_fn(observation):
        A = np.ones(nA, dtype=float)*epsilon/nA
        best_action = np.argmax(Q[observation])
        A[best_action] += (1.0 - epsilon)
        return A
    return policy_fn
def mc_control_epsilon_greedy(env, num_episodes, discount_factor=1.0, epsilon=0.1):
    return_sum = defaultdict(float)
    returns_count = defaultdict(float)
    Q = defaultdict(lambda :np.zeros(env.action_space.n))
    policy = make_epsilon_greedy_policy(Q, epsilon, env.action_space.n)
    for i_episode in range(1, num_episodes+1):
        if i_episode % 1000 == 0:
            print("\rEpisode{}/{}.".format(i_episode, num_episodes),end="")
            sys.stdout.flush()
        episode = []
        state = env._reset()
        for t in range(100):
            probs = policy(state)
            action = np.random.choice(np.arange(len(probs)), p=probs)
            next_state, reward, done, _ = env._step(action)
            episode.append((state, action, reward))
            if done:
                break
            state = next_state
        sa_in_episode = set([(tuple(x[0]), x[1]) for x in episode])
        for state, action in sa_in_episode:
            sa_pair = (state, action)
            first_occurence_idx = next(i for i, x in enumerate(episode) if x[0]==state and x[1]==action)
            G = sum([x[2]*(discount_factor**i) for i,x in enumerate(episode[first_occurence_idx:])])
            return_sum[sa_pair] += G
            returns_count[sa_pair] += 1.0
            Q[state][action] = return_sum[sa_pair]/returns_count[sa_pair]
    return Q, policy