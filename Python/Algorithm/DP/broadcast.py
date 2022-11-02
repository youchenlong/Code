"""
R为每一时刻用户访问量，
k次广播。
每次广播，之前的用户访问请求会被响应。
求一个广播方案，使所有用户等待时间之和最短。
"""

R = [3,4,0,5,2,7]
n = len(R)

c = [[[0 for k in range(3)] for j in range(n+1)] for i in range(n+1)]

for i in range(n):
    for j in range(i+1,n+1):
        c[i][j][1-1] = sum([R[t]*(j-t) for t in range(i,j)])

for k in range(2,3+1):
    for i in range(n):
        for j in range(i+k,n+1):
            c[i][j][k-1] = min([c[i][t][1-1]+c[t][j][k-1-1] for t in range(i+1,j)])

print(c[0][n][3-1])