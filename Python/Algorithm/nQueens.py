class nQueens:
    def __init__(self, n):
        self.n = n
        self.solutions = []
        self.places = [0 for i in range(n)]
    def valid(self, k):
        for i in range(k):
            if abs(self.places[i] - self.places[k]) == abs(i - k) or self.places[i] == self.places[k]:
                return False
        return True
    def dfs(self, k):
        if k == self.n:
            self.solutions.append(self.places.copy())
            return
        for j in range(self.n):
            self.places[k] = j
            if self.valid(k):
                self.dfs(k + 1)
    def solve(self):
        self.dfs(0)

q = nQueens(4)
q.solve()
print(q.solutions)
