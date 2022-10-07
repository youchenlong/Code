Value = [[(5, 5), (3, 6)], [(6, 3), (0, 0)]]
p1 = [0.75, 0.25]
p2 = [0.75, 0.25]
E_v1 = 0
E_v2 = 0
for i in range(len(Value)):
    for j in range(len(Value[0])):
        v1, v2 = Value[i][j]
        E_v1 += p1[i]*p2[j]*v1
        E_v2 += p1[i]*p2[j]*v2
print(E_v1)
print(E_v2)