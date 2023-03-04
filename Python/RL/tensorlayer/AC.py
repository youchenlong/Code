"""
Actor-Critic 
-------------
It uses TD-error as the Advantage.

Actor Critic History
----------------------
A3C > DDPG > AC

Advantage
----------
AC converge faster than Policy Gradient.

Disadvantage (IMPORTANT)
------------------------
The Policy is oscillated (difficult to converge), DDPG can solve
this problem using advantage of DQN.

Reference
----------
paper: https://papers.nips.cc/paper/1786-actor-critic-algorithms.pdf
View more on MorvanZhou's tutorial page: https://morvanzhou.github.io/tutorials/

Environment
------------
CartPole-v0: https://gym.openai.com/envs/CartPole-v0

A pole is attached by an un-actuated joint to a cart, which moves along a
frictionless track. The system is controlled by applying a force of +1 or -1
to the cart. The pendulum starts upright, and the goal is to prevent it from
falling over.

A reward of +1 is provided for every timestep that the pole remains upright.
The episode ends when the pole is more than 15 degrees from vertical, or the
cart moves more than 1.4 units from the center.


Prerequisites
--------------
tensorflow >=1.0.0a0
tensorlayer >=1.0.0

To run
------
python AC.py --train --env_id=CartPole-v1

"""
import argparse
import os
import random
import time

import gym
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

import tensorlayer as tl

tl.logging.set_verbosity(tl.logging.DEBUG)

# add arguments in command  --train/test_transformer
parser = argparse.ArgumentParser(description='Train or test_transformer neural net motor controller.')
parser.add_argument('--train', dest='train', action='store_true')
parser.add_argument('--test_transformer', dest='test_transformer', action='store_true')
parser.add_argument('--save_path', default=None, help='folder to save')
parser.add_argument('--seed', help='random seed', type=int, default=0)
parser.add_argument('--env_id', default='CartPole-v1', help='OpenGYM environment')
args = parser.parse_args()

random.seed(args.seed)
np.random.seed(args.seed)
tf.random.set_seed(args.seed)  # reproducible

env_id = args.env_id
env = gym.make(env_id)
env.seed(args.seed)

alg_name = 'AC'
print(alg_name)
time.sleep(5)

#####################  hyper parameters  ####################

TRAIN_EPISODES = 1000  # number of overall episodes for training
TEST_EPISODES = 10  # number of overall episodes for testing
MAX_STEPS = 500  # maximum time step in one episode
LAM = 0.9  # reward discount in TD error
LR_A = 0.001  # learning rate for actor
LR_C = 0.01  # learning rate for critic
in_dim = env.observation_space.shape
out_dim = env.action_space.n


###############################  Actor-Critic  ####################################


class Actor(object):

    def __init__(self):

        input_layer = tl.layers.Input([None, in_dim[0]], name='state')
        layer = tl.layers.Dense(
            n_units=30, act=tf.nn.relu6, W_init=tf.random_uniform_initializer(0, 0.01), name='hidden'
        )(input_layer)
        layer = tl.layers.Dense(n_units=out_dim, name='actions')(layer)
        self.model = tl.models.Model(inputs=input_layer, outputs=layer, name="Actor")

        self.model.train()
        self.optimizer = tf.optimizers.Adam(LR_A)

    def learn(self, state, action, td_error):
        with tf.GradientTape() as tape:
            _logits = self.model(np.array([state]))
            ## cross-entropy loss weighted by td-error (advantage),
            # the cross-entropy mearsures the difference of two probability distributions: the predicted logits and sampled action distribution,
            # then weighted by the td-error: small difference of real and predict actions for large td-error (advantage); and vice versa.
            _exp_v = tl.rein.cross_entropy_reward_loss(logits=_logits, actions=[action], rewards=td_error[0])
        grad = tape.gradient(_exp_v, self.model.trainable_weights)
        self.optimizer.apply_gradients(zip(grad, self.model.trainable_weights))
        return _exp_v

    def get_action(self, state, greedy=False):
        _logits = self.model(np.array([state]))
        _probs = tf.nn.softmax(_logits).numpy()
        if greedy:
            return np.argmax(_probs.ravel())
        return tl.rein.choice_action_by_probs(_probs.ravel())  # sample according to probability distribution

    def save(self):  # save trained weights
        path = os.path.join('model', '_'.join([alg_name, env_id]))
        if not os.path.exists(path):
            os.makedirs(path)
        tl.files.save_npz(self.model.trainable_weights, name=os.path.join(path, 'model_actor.npz'))

    def load(self):  # load trained weights
        path = os.path.join('model', '_'.join([alg_name, env_id]))
        tl.files.load_and_assign_npz(name=os.path.join(path, 'model_actor.npz'), network=self.model)


class Critic(object):

    def __init__(self):
        input_layer = tl.layers.Input([1, in_dim[0]], name='state')
        layer = tl.layers.Dense(
            n_units=30, act=tf.nn.relu6, W_init=tf.random_uniform_initializer(0, 0.01), name='hidden'
        )(input_layer)
        layer = tl.layers.Dense(n_units=1, act=None, name='value')(layer)
        self.model = tl.models.Model(inputs=input_layer, outputs=layer, name="Critic")
        self.model.train()

        self.optimizer = tf.optimizers.Adam(LR_C)

    def learn(self, state, reward, state_, done):
        d = 0 if done else 1
        v_ = self.model(np.array([state_]))
        with tf.GradientTape() as tape:
            v = self.model(np.array([state]))
            ## TD_error = r + d * lambda * V(newS) - V(S)
            td_error = reward + d * LAM * v_ - v
            loss = tf.square(td_error)
        grad = tape.gradient(loss, self.model.trainable_weights)
        self.optimizer.apply_gradients(zip(grad, self.model.trainable_weights))
        return td_error

    def save(self):  # save trained weights
        path = os.path.join('model', '_'.join([alg_name, env_id]))
        if not os.path.exists(path):
            os.makedirs(path)
        tl.files.save_npz(self.model.trainable_weights, name=os.path.join(path, 'model_critic.npz'))

    def load(self):  # load trained weights
        path = os.path.join('model', '_'.join([alg_name, env_id]))
        tl.files.load_and_assign_npz(name=os.path.join(path, 'model_critic.npz'), network=self.model)


if __name__ == '__main__':

    actor = Actor()
    critic = Critic()

    t0 = time.time()
    if args.train:
        all_episode_reward = []
        for episode in range(TRAIN_EPISODES):
            state = env.reset().astype(np.float32)
            # step = 0  # number of step in this episode
            episode_reward = 0  # rewards of all steps
            while True:

                action = actor.get_action(state)
                state_new, reward, done, info = env.step(action)
                state_new = state_new.astype(np.float32)
                # if done: reward = -20   # reward shaping trick
                episode_reward += reward
                # try:
                #     td_error = critic.learn(
                #         state, reward, state_new, done
                #     )  # learn Value-function : gradient = grad[r + lambda * V(s_new) - V(s)]
                #     actor.learn(state, action, td_error)  # learn Policy : true_gradient = grad[logPi(s, a) * td_error]
                # except KeyboardInterrupt:  # if Ctrl+C at running actor.learn(), then save model, or exit if not at actor.learn()
                #     actor.save()
                #     critic.save()
                td_error = critic.learn(
                    state, reward, state_new, done
                )  # learn Value-function : gradient = grad[r + lambda * V(s_new) - V(s)]
                actor.learn(state, action, td_error)  # learn Policy : true_gradient = grad[logPi(s, a) * td_error]

                state = state_new
                # step += 1

                # if done or step >= MAX_STEPS:
                #     break
                if done:
                    break

            print('Training  | Episode: {}/{}  | Episode Reward: {:.0f}  | Running Time: {:.4f}' \
                  .format(episode + 1, TRAIN_EPISODES, episode_reward, time.time() - t0))

            if episode == 0:
                all_episode_reward.append(episode_reward)
            else:
                all_episode_reward.append(all_episode_reward[-1] * 0.9 + episode_reward * 0.1)

            # Early Stopping for quick check
            # if step >= MAX_STEPS:
            #     print("Early Stopping")     # Hao Dong: it is important for this task
            #     break
        actor.save()
        critic.save()

        plt.plot(all_episode_reward)
        if not os.path.exists('image'):
            os.makedirs('image')
        plt.savefig(os.path.join('image', '_'.join([alg_name, env_id])))

    if args.test:
        actor.load()
        critic.load()

        for episode in range(TEST_EPISODES):
            episode_time = time.time()
            state = env.reset().astype(np.float32)
            # t = 0  # number of step in this episode
            episode_reward = 0
            while True:
                env.render()
                action = actor.get_action(state, greedy=True)
                state_new, reward, done, info = env.step(action)
                state_new = state_new.astype(np.float32)
                # if done: reward = -20

                episode_reward += reward
                state = state_new
                # t += 1

                # if done or t >= MAX_STEPS:
                #     print('Testing  | Episode: {}/{}  | Episode Reward: {:.0f}  | Running Time: {:.4f}' \
                #           .format(episode + 1, TEST_EPISODES, episode_reward, time.time() - t0))
                #     break
                if done:
                    print('Testing  | Episode: {}/{}  | Episode Reward: {:.0f}  | Running Time: {:.4f}' \
                          .format(episode + 1, TEST_EPISODES, episode_reward, time.time() - t0))
                    break
