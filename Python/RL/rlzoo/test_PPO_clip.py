import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import StochasticPolicyNetwork
from rlzoo.common.value_networks import ValueNetwork
from rlzoo.algorithms.dppo_clip.dppo_clip import DPPO_CLIP
import tensorflow as tf

n_workers = 4
env_id = 'Pendulum-v0'
env = [gym.make(env_id).unwrapped for i in range(n_workers)]
obs_space = env[0].observation_space
act_space = env[0].action_space

seed = [2 for _ in range(n_workers)]
set_seed(seed, env)

name = 'DPPO_CLIP'
hidden_dim = 64
num_hidden_layer = 2
critic = ValueNetwork(obs_space, [hidden_dim] * num_hidden_layer, name=name + '_value')
actor = StochasticPolicyNetwork(obs_space, act_space,
                                [hidden_dim] * num_hidden_layer,
                                trainable=True,
                                name=name + '_policy')
net_list = [critic, actor]

actor_lr = 1e-4
critic_lr = 2e-4
optimizers_list = [tf.optimizers.Adam(critic_lr), tf.optimizers.Adam(actor_lr)]
model = DPPO_CLIP(net_list, optimizers_list)

model.learn(env, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            n_workers=n_workers,
            plot_func=plot)

model.learn(env,  mode='test', render=True,
            test_episodes=10,
            max_steps=200)
