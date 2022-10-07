import math

v = [30, 15, 20]  # 金额
p = [0.9, 0.8, 0.5]  # 可靠性
m, n = 3, 105
dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
for x in range(n + 1):
    dp[0][x] = 1
for k in range(1, m + 1):
    dp[k][0] = 0
# 前k个部件
for k in range(1, m + 1):
    # 总金额为x
    for x in range(1, n - sum(v[k:]) + 1):
        temp = [0]
        # 购买j个元器件
        for j in range(1, math.floor(x / v[k - 1]) + 1):
            pkj = 1 - (1 - p[k - 1]) ** j
            temp.append(pkj * dp[k - 1][x - j * v[k - 1]])
        dp[k][x] = max(temp)
print(dp[m][n])
