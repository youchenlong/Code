import gym
from rlzoo.common.utils import set_seed
from rlzoo.common.value_networks import ValueNetwork
from rlzoo.common.policy_networks import StochasticPolicyNetwork
from rlzoo.algorithms.ac.ac import AC
import tensorflow as tf

# env_id = 'CartPole-v1'
env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 2
set_seed(seed, env)

actor = StochasticPolicyNetwork(obs_space, act_space, hidden_dim_list=2*[64])
critic = ValueNetwork(obs_space, activation=tf.nn.tanh, hidden_dim_list=2*[64], output_activation=tf.nn.tanh)
net_list = [actor, critic]
a_optimizer = tf.optimizers.Adam(1e-4)
c_optimizer = tf.optimizers.Adam(1e-4)
optimizers_list = [a_optimizer, c_optimizer]
model = AC(net_list, optimizers_list)

model.learn(env, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            save_interval=100)
model.learn(env, mode='test_transformer', render=True,
            test_episodes=10,
            max_steps=200)
