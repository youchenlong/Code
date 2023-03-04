import gym
import numpy as np
import tensorflow.compat.v1 as tf 
tf.disable_v2_behavior()
import random
from collections import deque 
import time

# Hyper Parameters:
FRAME_PER_ACTION = 1
GAMMA = 0.99 # decay rate of past observations
OBSERVE = 100. # timesteps to observe before training
EXPLORE = 50000. # frames over which to anneal epsilon
FINAL_EPSILON = 0.001#0.001 # final value of epsilon
INITIAL_EPSILON = 0.1#0.01 # starting value of epsilon
REPLAY_MEMORY = 4000 # number of previous transitions to remember
BATCH_SIZE = 32 # size of minibatch
UPDATE_TIME = 200

class BrainDQN():

    def __init__(self,actions):
        # init replay memory
        self.replayMemory = deque()
        # init some parameters
        self.timeStep = 0
        self.epsilon = INITIAL_EPSILON
        self.actions = actions
        # init Q network
        self.stateInput,self.QValue,self.W_fc1,self.b_fc1,self.W_fc2,self.b_fc2 = self.createQNetwork()
        # init Target Q Network
        self.stateInputT,self.QValueT,self.W_fc1T,self.b_fc1T,self.W_fc2T,self.b_fc2T = self.createQNetwork()
        self.copyTargetQNetworkOperation = [self.W_fc1T.assign(self.W_fc1),self.b_fc1T.assign(self.b_fc1),self.W_fc2T.assign(self.W_fc2),self.b_fc2T.assign(self.b_fc2)]
        self.createTrainingMethod()
        # saving and loading networks
        self.saver = tf.train.Saver()
        self.session = tf.InteractiveSession()
        self.session.run(tf.initialize_all_variables())
        checkpoint = tf.train.get_checkpoint_state("saved_networks")
        if checkpoint and checkpoint.model_checkpoint_path:
                self.saver.restore(self.session, checkpoint.model_checkpoint_path)
                print ("Successfully loaded:", checkpoint.model_checkpoint_path)
        else:
                print ("Could not find old network weights")

    def createQNetwork(self):
        # network weights
        STATE_DIM,ACTION_DIM = 4,self.actions
        W_fc1 = tf.Variable(tf.random_normal([STATE_DIM,100]))
        b_fc1 = tf.Variable(tf.zeros([100]))
        W_fc2 = tf.Variable(tf.random_normal([100,ACTION_DIM]))
        b_fc2 = tf.Variable(tf.zeros([ACTION_DIM]))
        # input layer
        stateInput = tf.placeholder('float', [None,STATE_DIM])
        # hidden layer
        h_fc1 = tf.nn.relu(tf.matmul(stateInput,W_fc1)+b_fc1)
        # Q Value layer
        QValue = tf.matmul(h_fc1,W_fc2)+b_fc2
        return stateInput,QValue,W_fc1,b_fc1,W_fc2,b_fc2

    def copyTargetQNetwork(self):
        self.session.run(self.copyTargetQNetworkOperation)

    def createTrainingMethod(self):
        self.actionInput = tf.placeholder("float",[None,self.actions])
        self.yInput = tf.placeholder("float", [None]) 
        Q_Action = tf.reduce_sum(tf.multiply(self.QValue, self.actionInput), reduction_indices = 1)
        self.cost = tf.reduce_mean(tf.square(self.yInput - Q_Action))
        self.trainStep = tf.train.AdamOptimizer(0.001).minimize(self.cost)

    def trainQNetwork(self):	
        # Step 1: obtain random minibatch from replay memory
        minibatch = random.sample(self.replayMemory,BATCH_SIZE)
        state_batch = [data[0] for data in minibatch]
        action_batch = [data[1] for data in minibatch]
        reward_batch = [data[2] for data in minibatch]
        nextState_batch = [data[3] for data in minibatch]
        # Step 1: calculate y
        y_batch = []
        QValue_batch = self.QValueT.eval(feed_dict={self.stateInputT:nextState_batch})
        for i in range(0,BATCH_SIZE):
            done = minibatch[i][4]
            if done:
                y_batch.append(reward_batch[i])
            else:
                y_batch.append(reward_batch[i] + GAMMA * np.max(QValue_batch[i]))
        self.trainStep.run(feed_dict={
            self.yInput : y_batch,
            self.actionInput : action_batch,
            self.stateInput : state_batch
            })
        # save network every 10000 iteration
        if self.timeStep % 10000 == 0:
            self.saver.save(self.session, 'saved_networks/' + 'network' + '-dqn', global_step = self.timeStep)
        if self.timeStep % UPDATE_TIME == 0:
            self.copyTargetQNetwork()
        
    def setPerception(self,nextState,action,reward,done):
        newState = nextState
        self.replayMemory.append((self.currentState,action,reward,newState,done))
        if len(self.replayMemory) > REPLAY_MEMORY:
            self.replayMemory.popleft()
        if self.timeStep > OBSERVE:
            # Train the network
            self.trainQNetwork()
        # print info
        state = ""
        if self.timeStep <= OBSERVE:
            state = "observe"
        elif self.timeStep > OBSERVE and self.timeStep <= OBSERVE + EXPLORE:
            state = "explore"
        else:
            state = "train"
        print ("TIMESTEP", self.timeStep, "/ STATE", state, \
            "/ EPSILON", self.epsilon)
        self.currentState = newState
        self.timeStep += 1

    def getAction(self):
        QValue = self.QValue.eval(feed_dict= {self.stateInput:[self.currentState]})[0]
        action = np.zeros(self.actions)
        action_index = 0
        if np.random.random() <= self.epsilon:
            action_index = np.random.choice(self.actions)
            action[action_index] = 1
        else:
            action_index = np.argmax(QValue)
            action[action_index] = 1
        # change episilon
        if self.epsilon > FINAL_EPSILON and self.timeStep > OBSERVE:
            self.epsilon -= (INITIAL_EPSILON - FINAL_EPSILON)/EXPLORE
        return action
    
    def setInitState(self,state):
        self.currentState = state

def play():
    # Step 1: init BrainDQN
    actions = 2
    brain = BrainDQN(actions)
    # Step 1: init Game
    env = gym.make('CartPole-v0')
    # Step 3: play game
    while 1 != 0:
        total_reward = 0
        # Step 3.1: obtain init state
        state = env.reset()
        brain.setInitState(state)
        # Step 3.1: run the game
        while True:
            action = brain.getAction()
            nextState,reward,done,info = env.step(np.argmax(action))
            total_reward += reward
            brain.setPerception(nextState,action,reward,done)
            if not done:
                env.render()
            if done:
                print('reward:',total_reward)
                time.sleep(0.5)
                break

def main():
    play()

if __name__ == '__main__':
    main()