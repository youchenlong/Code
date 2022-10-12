import networkx as nx
import matplotlib.pyplot as plt

class graphColoring:
    def __init__(self, graph, m):
        self.graph = graph
        self.n = graph.number_of_nodes()
        self.m = m
        self.colors = [-1 for _ in range(self.n)]
        self.solutions = []
    def valid(self, k):
        for node in list(self.graph.adj[k+1]):
            if self.colors[k] == self.colors[node-1]:
                return False
        return True
    def dfs(self, k):
        if k == self.n:
            self.solutions.append(self.colors.copy())
            return
        for color in range(self.m):
            self.colors[k] = color
            if self.valid(k):
                self.dfs(k+1)
    def solve(self):
        self.dfs(0)


edges = [(1,2),(1,3),(1,4),(2,3),(2,4),(2,5),(3,4),(4,5)]
graph = nx.Graph(edges)
# m = 3
m = 4
coloring = graphColoring(graph, m)
coloring.solve()
print(coloring.solutions)
try:
    color_list = []
    all_colors = ['red', 'yellow', 'blue', 'green']
    for color in coloring.solutions[0]:
        color_list.append(all_colors[color])
    nx.draw(graph, node_color=color_list, with_labels=True)
    plt.show()
except:
    print('There is no solution for graph coloring')