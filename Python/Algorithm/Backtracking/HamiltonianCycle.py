import networkx as nx
import matplotlib.pyplot as plt

class HamiltonianCycle:
    def __init__(self, graph):
        self.graph = graph
        self.n = graph.number_of_nodes()
        for node in list(graph.nodes):
            self.graph.nodes[node]['status'] = 'unvisited'
        self.cycle = [-1 for _ in range(self.n+1)]
        self.solutions = []
    def dfs(self, k):
        if k == self.n-1:
            if self.cycle[k] in self.graph.adj[1]:
                self.cycle[k+1] = 1
                self.solutions.append(self.cycle.copy())
                self.cycle[k+1] = -1
            return
        for node in list(self.graph.adj[self.cycle[k]]):
            if self.graph.nodes[node]['status'] == 'unvisited':
                self.graph.nodes[node]['status'] = 'visited'
                self.cycle[k+1] = node
                self.dfs(k+1)
                self.graph.nodes[node]['status'] = 'unvisited'
                self.cycle[k+1] = -1
    def solve(self):
        self.graph.nodes[1]['status'] = 'visited'
        self.cycle[0] = 1
        self.dfs(0)

edges = [(1,2),(1,3),(1,7),(2,3),(2,8),(3,4),(3,6),(4,5),(5,6),(6,7),(7,8)]
# edges = [(1,1),(1,5),(1,3),(1,4),(1,5),(3,4)]
graph = nx.Graph(edges)
h = HamiltonianCycle(graph)
h.solve()
print(h.solutions)

try:
    cycle = h.solutions[0]
    for edge in graph.edges:
        graph.edges[edge]['color'] = 'blue'
    for i in range(len(cycle) - 1):
        graph.edges[(cycle[i], cycle[i + 1])]['color'] = 'red'
    color_list = [graph.edges[edge]['color'] for edge in graph.edges]
    nx.draw(graph, edge_color=color_list, with_labels=True)
    plt.show()
except:
    print('There is no Hamiltonian Cycle')