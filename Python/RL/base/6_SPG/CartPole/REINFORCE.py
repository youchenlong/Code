import gym
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
import time
import sys

class PolicyGradient:
    def __init__(self, n_actions, n_features, learning_rate=0.01, reward_decay=0.99):
        self.n_actions = n_actions
        self.n_features = n_features
        self.lr = learning_rate
        self.gamma = reward_decay
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []
        self.create_network()
        self.saver = tf.train.Saver()
        self.session = tf.InteractiveSession()
        self.session.run(tf.global_variables_initializer())
        checkpoint = tf.train.get_checkpoint_state("saved_networks")
        if checkpoint and checkpoint.model_checkpoint_path:
                self.saver.restore(self.session, checkpoint.model_checkpoint_path)
                print ("Successfully loaded:", checkpoint.model_checkpoint_path)
        else:
                print ("Could not find old network weights")
    def create_network(self):
        # network weights
        self.W_fc1 = tf.Variable(tf.random_normal([self.n_features, 20]))
        self.b_fc1 = tf.Variable(tf.zeros([20]))
        self.W_fc2 = tf.Variable(tf.random_normal([20, self.n_actions]))
        self.b_fc2 = tf.Variable(tf.zeros([self.n_actions]))
        # input layer
        self.tf_obs = tf.placeholder(tf.float32, [None, self.n_features])
        self.tf_acts = tf.placeholder(tf.int32, [None, ])
        self.tf_vt = tf.placeholder(tf.float32, [None, ])
        # hidden layer
        h_fc = tf.nn.relu(tf.matmul(self.tf_obs, self.W_fc1)+self.b_fc1)
        # output layer
        all_act = tf.matmul(h_fc, self.W_fc2)+self.b_fc2
        self.all_act_prob = tf.nn.softmax(all_act)
        neg_log_prob = tf.nn.sparse_softmax_cross_entropy_with_logits(logits=all_act, labels=self.tf_acts)
        loss = tf.reduce_mean(neg_log_prob * self.tf_vt)
        self.train_op = tf.train.AdamOptimizer(self.lr).minimize(loss)
    def choose_action(self, observation):
        prob_weights = self.session.run(self.all_act_prob, feed_dict={self.tf_obs:observation[np.newaxis,:]})
        action = np.random.choice(range(prob_weights.shape[1]), p=prob_weights.ravel())
        return action
    def store_transition(self, s, a, r):
        self.ep_obs.append(s)
        self.ep_as.append(a)
        self.ep_rs.append(r)
    def _discount_and_norm_rewards(self):
        discounted_ep_rs = np.zeros_like(self.ep_rs)
        running_add = 0
        for t in reversed(range(0, len(self.ep_rs))):
            running_add = running_add * self.gamma + self.ep_rs[t]
            discounted_ep_rs[t] = running_add
        discounted_ep_rs -= np.mean(discounted_ep_rs)
        discounted_ep_rs /= np.std(discounted_ep_rs)
        return discounted_ep_rs
    def learn(self):
        discounted_ep_rs_norm = self._discount_and_norm_rewards()
        self.session.run(self.train_op, feed_dict={
            self.tf_obs: np.vstack(self.ep_obs),
            self.tf_acts: np.array(self.ep_as),
            self.tf_vt: discounted_ep_rs_norm
        })
        self.ep_obs, self.ep_as, self.ep_rs = [], [], []
        return discounted_ep_rs_norm

def play():
    env = gym.make('CartPole-v0')
    agent = PolicyGradient(n_actions=env.action_space.n, n_features=env.observation_space.shape[0])
    episodes = 1000
    for i_episode in range(1, episodes+1):
        if i_episode % 100 == 0:
            print('\rEpisode {}/{}'.format(i_episode, episodes), end='')
            sys.stdout.flush()
        total_reward = 0
        state = env.reset()
        while True:
            action = agent.choose_action(state)
            nextState, reward, done, info = env.step(action)
            total_reward += reward
            agent.store_transition(state, action, reward)
            if not done:
                env.render()
            if done:
                agent.learn()
                print(total_reward)
                time.sleep(0.5)
                break
            state = nextState
        # if i_episode % 100 == 0:
        #     agent.saver.save(agent.session, 'saved_networks/' + 'REINFORCE', global_step = 1000+i_episode)

if __name__ == '__main__':
    play()