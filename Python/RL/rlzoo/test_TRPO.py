import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import StochasticPolicyNetwork
from rlzoo.common.value_networks import ValueNetwork
from rlzoo.algorithms.trpo.trpo import TRPO
import tensorflow as tf

# env_id = 'CartPole-v1'
env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 2
set_seed(seed, env)

name = 'TRPO'
hidden_dim = 64
num_hidden_layer = 2
critic = ValueNetwork(obs_space, [hidden_dim] * num_hidden_layer, name=name + '_value')
actor = StochasticPolicyNetwork(obs_space, act_space, [hidden_dim] * num_hidden_layer, name=name + '_policy')
net_list = [critic, actor]

c_optimizer = tf.optimizers.Adam(1e-3)
optimizers_list = [c_optimizer]

model = TRPO(net_list, optimizers_list, damping_coeff=0.1, cg_iters=10, delta=0.01)

model.learn(env, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            plot_func=plot)

model.learn(env, mode='test', render=True,
            test_episodes=10,
            max_steps=200)
