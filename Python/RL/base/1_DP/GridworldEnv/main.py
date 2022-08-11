from GridworldEnv import GridworldEnv
from PolicyIteration import policy_improvement
from ValueIteration import value_iteration
# from PolicyIteration import change_policy


if __name__ == "__main__":
    env = GridworldEnv()
    # policy, v = policy_improvement(env)
    policy, v = value_iteration(env)
    # update_policy_type = change_policy(policy)

    print(policy)
    print(v.reshape(env.shape))
    # print(update_policy_type)