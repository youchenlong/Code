S1='AACAGTTACC'
S2='TAAGGTCA'
Cm, Cg = 1, 1
m = len(S1)
n = len(S2)
dp = [[0 for j in range(n+1)] for i in range(m+1)]
direction = [[' ' for j in range(n+1)] for i in range(m+1)]


def update(i, j):
    if S1[i] == S2[j]:
        if dp[i+1][j+1] == min(dp[i+1][j+1], dp[i+1][j]+Cg, dp[i][j+1]+Cg):
            dp[i][j] = dp[i+1][j+1]
            direction[i][j] = '↖'
        elif dp[i+1][j]+Cg == min(dp[i+1][j+1], dp[i+1][j]+Cg, dp[i][j+1]+Cg):
            dp[i][j] = dp[i+1][j]+Cg
            direction[i][j] = '↑'
        else:
            dp[i][j] = dp[i][j+1]+Cg
            direction[i][j] = '←'
    else:
        if dp[i+1][j+1]+Cm == min(dp[i+1][j+1]+Cm, dp[i+1][j]+Cg, dp[i][j+1]+Cg):
            dp[i][j] = dp[i+1][j+1]+Cm
            direction[i][j] = '↖'
        elif dp[i+1][j]+Cg == min(dp[i+1][j+1]+Cm, dp[i+1][j]+Cg, dp[i][j+1]+Cg):
            dp[i][j] = dp[i+1][j]+Cg
            direction[i][j] = '↑'
        else:
            dp[i][j] = dp[i][j+1]+Cg
            direction[i][j] = '←'

for j in range(n+1):
    dp[m][j] = n-j
for i in range(m+1):
    dp[i][n] = m-i
for i in reversed(range(m)):
    for j in reversed(range(n)):
        # 替换 删除 插入
        update(i, j)
for i in range(m+1):
    for j in range(n+1):
        print(direction[i][j], end=' ')
    print()
print(dp[0][0])
