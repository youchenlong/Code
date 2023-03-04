import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import DeterministicPolicyNetwork
from rlzoo.common.value_networks import QNetwork
from rlzoo.algorithms.ddpg.ddpg import DDPG
import tensorflow as tf

env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 2
set_seed(seed, env)

name = 'DDPG'
num_hidden_layer = 2
hidden_dim = 64
actor = DeterministicPolicyNetwork(obs_space, act_space, [hidden_dim] * num_hidden_layer)
critic = QNetwork(obs_space, act_space, [hidden_dim] * num_hidden_layer)
actor_target = DeterministicPolicyNetwork(obs_space, act_space, [hidden_dim] * num_hidden_layer, trainable=False)
critic_target = QNetwork(obs_space, act_space, [hidden_dim] * num_hidden_layer, trainable=False)
net_list = [critic, critic_target, actor, actor_target]

actor_lr = 1e-3
critic_lr = 2e-3
optimizers_list = [tf.optimizers.Adam(critic_lr), tf.optimizers.Adam(actor_lr)]

replay_buffer_size = 300
model = DDPG(net_list, optimizers_list, replay_buffer_size)

model.learn(env, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            noise_scale=1., noise_scale_decay=0.995,
            plot_func=plot)

model.learn(env,  mode='test_transformer', render=True,
            test_episodes=10,
            max_steps=200)

