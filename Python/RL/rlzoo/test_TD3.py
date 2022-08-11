import gym
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import DeterministicPolicyNetwork
from rlzoo.common.value_networks import QNetwork
from rlzoo.algorithms.td3.td3 import TD3
import tensorflow as tf

env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
act_space = env.action_space
obs_space = env.observation_space

seed = 2
set_seed(seed, env)

num_hidden_layer = 2
hidden_dim = 64
with tf.name_scope('TD3'):
    with tf.name_scope('Q_Net1'):
        q_net1 = QNetwork(obs_space, act_space,
                          hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Q_Net2'):
        q_net2 = QNetwork(obs_space, act_space,
                          hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Target_Q_Net1'):
        target_q_net1 = QNetwork(obs_space, act_space,
                                 hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Target_Q_Net2'):
        target_q_net2 = QNetwork(obs_space, act_space,
                                 hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Policy'):
        policy_net = DeterministicPolicyNetwork(obs_space, act_space,
                                                hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Target_Policy'):
        target_policy_net = DeterministicPolicyNetwork(obs_space, act_space,
                                                       hidden_dim_list=num_hidden_layer * [hidden_dim])
net_list = [q_net1, q_net2, target_q_net1, target_q_net2, policy_net, target_policy_net]

q_lr, policy_lr = 3e-4, 3e-4
q_optimizer1 = tf.optimizers.Adam(q_lr)
q_optimizer2 = tf.optimizers.Adam(q_lr)
policy_optimizer = tf.optimizers.Adam(policy_lr)
optimizers_list = [q_optimizer1, q_optimizer2, policy_optimizer]

model = TD3(net_list, optimizers_list)

model.learn(env, mode='train', render=False,
            train_episodes=300,
            max_steps=200,
            explore_noise_scale=1.0, eval_noise_scale=0.5,
            plot_func=plot)

model.learn(env, mode='test', render=True,
            test_episodes=10,
            max_steps=200)
