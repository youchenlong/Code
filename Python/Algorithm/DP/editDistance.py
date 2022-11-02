"""
增加和删除代价为1，修改代价为2
"""

str1 = 'love'
str2 = 'lolpe'
cost_insert = 1
cost_delete = 1
cost_update = 2
m, n = len(str1), len(str2)
D = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(m+1):
    D[i][0] = cost_delete * i
for j in range(n+1):
    D[0][j] = cost_insert * j
for i in range(1, m+1):
    for j in range(1, n+1):
        # 字符相等
        if str1[i-1] == str2[j-1]:
            D[i][j] = min(D[i - 1][j - 1], D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert)
        # 字符不相等
        else:
            D[i][j] = min(D[i - 1][j - 1] + cost_update, D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert)
print(D[m][n])