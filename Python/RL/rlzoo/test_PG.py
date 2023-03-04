import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import StochasticPolicyNetwork
from rlzoo.algorithms import PG
import tensorflow as tf

# env_id = 'CartPole-v1'
env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 2
set_seed(seed, env)

name = 'PG'
policy_net = StochasticPolicyNetwork(obs_space, act_space, hidden_dim_list=[32])
net_list = [policy_net]

policy_optimizer = tf.optimizers.Adam(0.001)
optimizers_list = [policy_optimizer]
pg = PG(net_list, optimizers_list)

pg.learn(env, mode='train', render=False,
         train_episodes=1000,
         max_steps=200,
         plot_func=plot)
pg.learn(env, mode='test_transformer', render=True,
         test_episodes=10,
         max_steps=200)