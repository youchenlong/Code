investment = [[0, 20, 50, 65, 80, 85, 85],
              [0, 20, 45, 50, 55, 60, 65],
              [0, 25, 60, 85, 100, 110, 115],
              [0, 25, 40, 50, 60, 65, 70]]
assets = 6
m, n = len(investment), assets
D = [[0 for j in range(n+1)] for i in range(m+1)]
T = [[0 for j in range(n+1)] for i in range(m+1)]
for i in range(1, m+1):
    for j in range(1, n+1):
        maxv, maxt = 0, 0
        # 投资第j个工厂t万元
        for t in range(j+1):
            if D[i-1][j-t]+investment[i-1][t] > maxv:
                maxv = D[i-1][j-t]+investment[i-1][t]
                maxt = t
        D[i][j] = maxv
        T[i][j] = maxt
i, j = m, n
investScheme = []
while i > 0:
    print(i, j)
    investScheme.insert(0, T[i][j])
    j = j - T[i][j]
    i = i - 1
print(investScheme)