import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.value_networks import QNetwork
from rlzoo.algorithms import DQN
import tensorflow as tf

env_id = 'CartPole-v1'
# env_id = 'MountainCar-v0'
env = gym.make(env_id)
obs_space = env.observation_space
act_space = env.action_space
seed = 0
set_seed(seed, env)

name = 'DQN'
Q_net = QNetwork(obs_space, act_space, hidden_dim_list=[64], activation=tf.nn.tanh, state_only=True, dueling=False)
net_list = [Q_net]
optimizer = tf.optimizers.Adam(5e-3, epsilon=1e-5)
optimizers_list = [optimizer]
dqn = DQN(net_list,
          optimizers_list,
          buffer_size=1000,
          double_q=False,
          dueling=False,
          prioritized_replay=True, prioritized_alpha=0.2, prioritized_beta0=0.5)
dqn.learn(env, mode='train', render=False,
          train_episodes=1000,
          max_steps=200,
          learning_starts=100,
          plot_func=plot)
dqn.learn(env, mode='test', render=True,
          test_episodes=10,
          max_steps=200)



