import gym
import time

# env_id = 'BreakoutNoFrameskip-v4'
# env_id = 'Pendulum-v0'
# env_id = 'CartPole-v1'
env_id = 'MountainCar-v0'
env = gym.make(env_id)
obs_space = env.observation_space
act_space = env.action_space
print(obs_space)
print(act_space)
o = env.reset()
while True:
    env.render()
    a = env.action_space.sample()
    o, r, done, _ = env.step(a)
    if done:
        break
env.close()