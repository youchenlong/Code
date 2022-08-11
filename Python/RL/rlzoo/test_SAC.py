from rlzoo.algorithms.sac.sac import SAC
from rlzoo.common.utils import set_seed, plot
from rlzoo.common.policy_networks import *
from rlzoo.common.value_networks import *
import gym

env_id = 'Pendulum-v0'
env = gym.make(env_id).unwrapped
obs_space = env.observation_space
act_space = env.action_space

seed = 2
set_seed(seed, env)

num_hidden_layer = 2
hidden_dim = 64
with tf.name_scope('SAC'):
    with tf.name_scope('Q_Net1'):
        soft_q_net1 = QNetwork(obs_space, act_space,
                               hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Q_Net2'):
        soft_q_net2 = QNetwork(obs_space, act_space,
                               hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Target_Q_Net1'):
        target_soft_q_net1 = QNetwork(obs_space, act_space,
                                      hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Target_Q_Net2'):
        target_soft_q_net2 = QNetwork(obs_space, act_space,
                                      hidden_dim_list=num_hidden_layer * [hidden_dim])
    with tf.name_scope('Policy'):
        policy_net = StochasticPolicyNetwork(obs_space, act_space,
                                             hidden_dim_list=num_hidden_layer * [hidden_dim],
                                             output_activation=None,
                                             state_conditioned=True)
net_list = [soft_q_net1, soft_q_net2, target_soft_q_net1, target_soft_q_net2, policy_net]

soft_q_lr, policy_lr, alpha_lr = 3e-4, 3e-4, 3e-4
soft_q_optimizer1 = tf.optimizers.Adam(soft_q_lr)
soft_q_optimizer2 = tf.optimizers.Adam(soft_q_lr)
policy_optimizer = tf.optimizers.Adam(policy_lr)
alpha_optimizer = tf.optimizers.Adam(alpha_lr)
optimizers_list = [soft_q_optimizer1, soft_q_optimizer2, policy_optimizer, alpha_optimizer]

model = SAC(net_list, optimizers_list)

model.learn(env, mode='train', AUTO_ENTROPY=True, render=False,
            train_episodes=300,
            max_steps=200,
            plot_func=plot)

model.learn(env, mode='test', render=True,
            test_episodes=10,
            max_steps=200)
