from HalftenEnv import HalftenEnv
from on_policy import mc_control_epsilon_greedy

env = HalftenEnv()
Q, policy = mc_control_epsilon_greedy(env, num_episodes=50000, epsilon=0.1)