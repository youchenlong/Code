class boatLoading:
    def __init__(self, containers, volume1, volume2):
        self.containers = containers
        self.total = [volume1, volume2]
        self.used = [0, 0]
        self.scheme = [-1 for _ in range(len(containers))]
        self.solutions = []

    def valid(self, i, k):
        if self.used[i] + self.containers[k] > self.total[i]:
            return False
        return True

    def dfs(self, k):
        if k == len(self.containers):
            self.solutions.append(self.scheme.copy())
            return
        for i in range(2):
            if self.valid(i, k):
                self.used[i] += self.containers[k]
                self.scheme[k] = i
                self.dfs(k + 1)
                self.used[i] -= self.containers[k]

    def solve(self):
        self.dfs(0)


containers = [10, 40, 40]
# containers = [20, 40, 40]
volume1 = 50
volume2 = 50
loading = boatLoading(containers, volume1, volume2)
loading.solve()
print(loading.solutions)
