class continuousPostage:
    def __init__(self, stampval, m):
        self.stampval = stampval
        self.stampval.insert(0, 0)
        self.n = len(stampval)
        self.m = m
        self.scheme = [-1 for i in range(m)]
        self.solutions = []
        self.result = 0
    def dfs(self, k):
        if k == self.m:
            self.solutions.append(sum(self.scheme))
            return
        for i in range(self.n):
            self.scheme[k] = self.stampval[i]
            self.dfs(k+1)
    def solve(self):
        self.dfs(0)
        self.solutions = list(set(self.solutions))
        for i in range(len(self.solutions)):
            if i != self.solutions[i]:
                return
            self.result = self.solutions[i]


stampval = [1, 3, 11, 15, 32]
# stampval = [1, 6, 10, 20, 30]
m = 4
postage = continuousPostage(stampval, m)
postage.solve()
print(postage.result)


