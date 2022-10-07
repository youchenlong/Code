import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1)

class Bandit:
    def __init__(self, k):
        self.k = 10
        # self.q = np.array(np.random.normal(loc=0.0, scale=1.0, size=k))
        self.q = np.array([0.2,-0.8,1.5,0.4,1.2,-1.5,-0.2,1.8,0.8,-0.6])
    def step(self, action):
        reward = np.random.normal(loc=self.q[action], scale=1.0)
        return reward

class Agent:
    def __init__(self, env, epsilon=0.0, c=0.0):
        self.actions = env.k
        self.Q = np.zeros(env.k, dtype=float)
        self.N = np.zeros(env.k, dtype=int)
        self.epsilon = epsilon
        self.c = c
    def get_action(self, t=1):
        # 置信上界算法
        if self.c > 0.0:
            return np.argmax(self.Q + self.c * np.sqrt(np.log(t) / self.N))
        # epsilon贪心策略
        if np.abs(np.random.normal(loc=0.0,scale=1.0)) < self.epsilon:
            return np.random.choice(self.actions)
        else:
            return np.argmax(self.Q)
    def update(self, action, reward):
        self.N[action] += 1
        self.Q[action] += 1.0 / self.N[action] * (reward - self.Q[action])


def train(env, agent, steps):
    rewards = []
    for t in range(steps):
        action = agent.get_action(t)
        reward = env.step(action)
        agent.update(action, reward)
        if t==0:
            rewards.append(reward)
        else:
            rewards.append(rewards[-1] * 0.99 + reward * 0.01)
        print('step:{}, action:{}, reward:{}'.format(t, action, reward))
    return rewards

k = 10
env = Bandit(k=10)
e_greedy_agent = Agent(env, epsilon=0.1)
UCB_agent = Agent(env, c=1)

steps = 2000
e_rewards = train(env, e_greedy_agent, steps)
UCB_rewards = train(env, UCB_agent, steps)

fig, ax = plt.subplots()
ax.plot(e_rewards, color='green', label='e-greedy')
ax.plot(UCB_rewards, color='blue', label='UCB')
plt.legend()
# plt.savefig('exploration.png')
plt.show()

