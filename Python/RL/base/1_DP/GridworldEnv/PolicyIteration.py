import numpy as np
from GridworldEnv import GridworldEnv
import time

# 策略评估
def policy_eval(policy, env, discount_factor=1, threshold=0.00001):
    # policy--策略
    # env--环境
    # discount_factor--折扣因子
    # threshold--阈值 

    # 状态值函数
    V = np.zeros(env.nS)
    # i = 0
    while True:
        value_delta = 0
        for s in range(env.nS):
            v = 0
            for a, action_prob in enumerate(policy[s]):
                for prob, next_state, reward, done in env.P[s][a]:
                    v += action_prob * prob * (reward + discount_factor * V[next_state])
            value_delta = max(value_delta, np.abs(v - V[s]))
            V[s] = v
        print(V.reshape(env.shape))
        print()
        time.sleep(0.05)
        # i += 1
        # 收敛时退出
        if value_delta < threshold:
            break
    print("converged, stop for 10 seconds")
    time.sleep(10)
    return np.array(V)

# 输入行为值函数，返回策略
def get_max_index(Q):
    indexs = []
    policy_arr = np.zeros(len(Q))
    action_max_value = np.max(Q)
    for i in range(len(Q)):
        action_value = Q[i]
        if action_value == action_max_value:
            indexs.append(i)
            policy_arr[i] = 1
    return indexs, policy_arr

# def change_policy(policy):
#     action_tuple = []
#     for p in policy:
#         indexs, policy_arr = get_max_index(p)
#         action_tuple.append(tuple(indexs))
#     return action_tuple

# i_num = 1
# 策略改进
def policy_improvement(env, policy_eval_fn=policy_eval, discount_factor=1.0):
    # 策略
    policy = np.ones([env.nS, env.nA])/env.nA
    while True:
        # global i_num
        # 策略评估
        V = policy_eval_fn(policy, env, discount_factor)
        policy_stable = True
        # 遍历各状态，检查策略是否稳定
        for s in range(env.nS):
            chosen_a = np.argmax(policy[s])
            # 行为值函数
            Q = np.zeros(env.nA)
            for a in range(env.nA):
                for prob, next_state, reward, done in env.P[s][a]:
                    Q[a] += prob * (reward + discount_factor * V[next_state])
            best_a_arr, policy_arr = get_max_index(Q)
            if chosen_a not in best_a_arr:
                policy_stable = False
            policy[s] = policy_arr
        # i_num += 1
        if policy_stable:
            return policy, V