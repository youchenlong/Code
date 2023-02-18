"""
增加，删除，修改的代价为1
"""

str1 = "AACAGTTACC"
str2 = "TAAGGTCA"
cost_insert = 1
cost_delete = 1
cost_update = 1
m, n = len(str1), len(str2)
D = [[0 for j in range(n+1)] for i in range(m+1)]
T = [[' ' for j in range(n)] for i in range(m)]
for i in range(m+1):
    D[i][0] = cost_delete * i
for j in range(n+1):
    D[0][j] = cost_insert * j
for i in range(1, m+1):
    for j in range(1, n+1):
        # 字符相等
        if str1[i-1] == str2[j-1]:
            if D[i-1][j-1] == min(D[i - 1][j - 1], D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert):
                D[i][j] = D[i-1][j-1]
                T[i-1][j-1] = '\\'
            elif D[i - 1][j] + cost_delete == min(D[i - 1][j - 1], D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert):
                D[i][j] = D[i-1][j] + cost_delete
                T[i-1][j-1] = '|'
            else:
                D[i][j] = D[i][j-1] + cost_insert
                T[i-1][j-1] = '-'
        # 字符不相等
        else:
            # if D[i][j]+cost_update == min(D[i - 1][j - 1] + cost_update, D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert):                                    D[i][j - 1] + cost_insert):
            if D[i-1][j-1]+cost_update == min(D[i - 1][j - 1] + cost_update, D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert):
                D[i][j] = D[i-1][j-1] + cost_update
                T[i-1][j-1] = '\\'
            elif D[i - 1][j] + cost_delete == min(D[i - 1][j - 1], D[i - 1][j] + cost_delete, D[i][j - 1] + cost_insert):
                D[i][j] = D[i-1][j] + cost_delete
                T[i-1][j-1] = '|'
            else:
                D[i][j] = D[i][j-1] + cost_insert
                T[i-1][j-1] = '-'

for i in range(m):
    for j in range(n):
        print(T[i][j], end=' ')
    print("\n")
print(D[m][n])