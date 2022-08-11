import gym
import numpy as np
import time
from collections import defaultdict

def make_random_policy(nA):
    def policy_fn(observation):
        A = np.ones(nA)/nA
        return A
    return policy_fn

def make_greedy_policy(Q):
    def policy_fn(state):
        A = np.zeros_like(Q[state], dtype=float)
        best_action = np.argmax(Q[state])
        A[best_action] = 1.0
        return A
    return policy_fn
    
def mc_control_importance_sampling(env, num_episodes, behavior_policy, discount_factor=1.0):
    Q = defaultdict(lambda : np.zeros(env.action_space.n))
    C = defaultdict(lambda: np.zeros(env.action_space.n))
    target_policy = make_greedy_policy(Q)
    for i_episode in range(1, num_episodes+1):
        if i_episode % 1000 == 0:
            print('\rEpisode{}/{}'.format(i_episode, num_episodes))
            sys.stdout.flush()
        episode = []
        state = env.reset()
        for t in range(100):
            probs = behavior_policy(state)
            action = np.random.choice(np.arange(len(probs)), p=probs)
            next_state, reward, done, _ = env.step(action)
            episode.append((state, action, reward))
            if done:
                break
            state = next_state
        G = 0.0
        W = 1.0
        for t in range(len(episode))[::-1]:
            state, action, reward = episode[t]
            G = discount_factor * G + reward
            C[state][action] += W
            Q[state][action] += (W / C[state][action]) * (G - Q[state][action])
            if action != np.argmax(target_policy(state)):
                break
            W = W + 1.0 / behavior_policy(state)[action]
        return Q, target_policy

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
    env = gym.make('Blackjack-v1')
    random_policy = make_random_policy(env.action_space.n)
    run_game(env, policy=random_policy, episodes=500)
    Q, policy = mc_control_importance_sampling(env, num_episodes=500, behavior_policy=random_policy)
    run_game(env, policy=policy, episodes=500)
    env.close()
