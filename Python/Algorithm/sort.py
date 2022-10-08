import random
random.seed(1)
random.randint()
arr = [2, 1, 3, 5, 4, 6, 8, 7, 10, 9]

def bubbleSort(arr):
    # 无需部分小的元素向前移动直到有序部分末尾
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

def insertSort(arr):
    # 无序部分第一个元素插入到有序部分的合适位置
    n = len(arr)
    for i in range(1,n):
        k = i
        for j in range(i-1,-1,-1):
            if arr[k] < arr[j]:
                k = j
            else:
                break
        arr[k], arr[i] = arr[i], arr[k]

def selectionSort(arr):
    # 选择无序部分的最小元素放到有序部分的末尾
    n = len(arr)
    for i in range(n-1):
        k = i
        for j in range(i+1, n):
            if arr[j] < arr[k]:
                k = j
        arr[i], arr[k] = arr[k], arr[i]

# bubbleSort(arr)
# insertSort(arr)
# selectionSort(arr)
print(arr)
