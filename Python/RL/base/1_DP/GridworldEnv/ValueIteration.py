import numpy as np

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
# 值迭代
def value_iteration(env, threshold=0.0001, discount_factor=1.0):
    # global i_num

    # 输入状态值函数，返回行为值函数
    def one_step_lookahead(s, V):
        Q = np.zeros(env.nA)
        for a in range(env.nA):
            for prob, next_state, reward, done in env.P[s][a]:
                Q[a] += prob * (reward + discount_factor * V[next_state])
        return Q
    V = np.zeros(env.nS)
    while True:
        delta = 0
        for s in range(env.nS):
            Q = one_step_lookahead(s, V)
            bestQ = np.max(Q)
            delta = max(delta, np.abs(bestQ - V[s]))
            V[s] = bestQ
        # i_num += 1
        print(V.reshape(env.shape))
        if delta < threshold:
            break
    policy = np.zeros([env.nS, env.nA])
    for s in range(env.nS):
        Q = one_step_lookahead(s, V)
        best_a_arr, policy_arr = get_max_index(Q)
        policy[s] = policy_arr
    return policy, V