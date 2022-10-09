class sumOfSub:
    def __init__(self, arr, target):
        self.arr = arr
        self.target = target
        self.select = [0 for _ in range(len(arr))]
        self.total = 0
        self.solutions = []
    def dfs(self, k):
        if self.total >= self.target:
            if self.total == self.target:
                self.solutions.append(self.select.copy())
            return
        if k < len(self.arr):
            self.select[k] = 1
            self.total = self.total + self.arr[k]
            self.dfs(k+1)
            self.select[k] = 0
            self.total = self.total - self.arr[k]
            self.dfs(k+1)
    def solve(self):
        self.dfs(0)

arr = [12,10,5,18,15,13]
target = 30
s = sumOfSub(arr, target)
s.solve()
print(s.solutions)

