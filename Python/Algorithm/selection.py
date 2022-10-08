"""
查找第k小的元素，要求不进行排序
提示：使用分治法
"""

import numpy as np

def selection(arr, k):
    assert len(arr) > 0, 'the input array is empty!'
    v = arr[0]
    S1, S2, S3 = [], [], []
    for x in arr:
        if x < v:
            S1.append(x)
        elif x == v:
            S2.append(x)
        else:
            S3.append(x)
    l1, l2, l3 = len(S1), len(S2), len(S3)
    if k < l1:
        return selection(S1, k)
    elif k < l1 + l2:
        return v
    else:
        return selection(S3, k-l1-l2)

k = 10
arr = np.random.randint(0, 100, 2*k)
print(arr)
res = selection(arr, k)
print(np.median(arr))
print(res)