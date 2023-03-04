import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.algorithms.ppo_penalty.ppo_penalty import PPO_PENALTY
from rlzoo.common.policy_networks import StochasticPolicyNetwork
from rlzoo.common.value_networks import ValueNetwork
import tensorflow as tf

env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 1
set_seed(seed, env)

name = 'PPO_PENALTY'
hidden_dim = 64
num_hidden_layer = 2
critic = ValueNetwork(obs_space, [hidden_dim] * num_hidden_layer, name=name + '_value')
actor = StochasticPolicyNetwork(obs_space, act_space, [hidden_dim] * num_hidden_layer,
                                output_activation=tf.nn.tanh, name=name + '_policy')
net_list = [critic, actor]

actor_lr = 1e-4
critic_lr = 2e-4
optimizers_list = [tf.optimizers.Adam(critic_lr), tf.optimizers.Adam(actor_lr)]

model = PPO_PENALTY(net_list, optimizers_list,)

model.learn(env, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            plot_func=plot)

model.learn(env, mode='test_transformer', render=True,
            test_episodes=10,
            max_steps=200)
