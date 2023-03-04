import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import StochasticPolicyNetwork
from rlzoo.common.value_networks import ValueNetwork
from rlzoo.algorithms.a3c.a3c import A3C
import tensorflow as tf

# env_id = 'CartPole-v1'
env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 2
set_seed(seed, env)

num_workers = 2
all_net_list = []
for i in range(num_workers + 1):
    actor = StochasticPolicyNetwork(obs_space, act_space, hidden_dim_list=2*[64], activation=tf.nn.relu)
    critic = ValueNetwork(obs_space, hidden_dim_list=2*[64], activation=tf.nn.relu)
    net_list = [actor, critic]
    all_net_list.append(net_list)

a_optimizer = tf.optimizers.RMSprop(1e-3)
c_optimizer = tf.optimizers.RMSprop(1e-3)
optimizers_list = [a_optimizer, c_optimizer]

model = A3C(all_net_list, optimizers_list)

env_list = []
for i in range(num_workers):
    env_list.append(gym.make(env_id).unwrapped)
model.learn(env_list, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            n_workers=num_workers,
            plot_func=plot)
model.learn(env_list, mode='test_transformer', render=True,
            test_episodes=10,
            max_steps=200)
