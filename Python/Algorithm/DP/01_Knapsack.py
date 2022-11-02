volume = 12
weight = [4, 6, 2, 2, 5, 1]
value = [8, 10, 6, 3, 7, 2]
m, n = len(weight), volume
D = [[0 for j in range(n+1)] for i in range(m+1)]
precede = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        # 物品能装下
        if j >= weight[i-1]:
            # 装
            if D[i-1][j-weight[i-1]]+value[i-1] > D[i-1][j]:
                D[i][j] = D[i-1][j-weight[i-1]]+value[i-1]
                precede[i][j] = j-weight[i-1]
            # 不装
            else:
                D[i][j] = D[i-1][j]
                precede[i][j] = j
        # 物品不能装下
        else:
            D[i][j] = D[i-1][j]
            precede[i][j] = j
i, j = m, n
items = []
while i > 0:
    if precede[i][j] == precede[i-1][j]:
        i = i - 1
        j = j
    else:
        items.append(i-1)
        i = i - 1
        j = j - weight[i]
print(items)
