import networkx as nx
import matplotlib.pyplot as plt

# nodes = [1,2,3,4,5,6]
# inf = 10000
# m = [[0, 50, inf, 40, 25, 10],
#      [50, 0, 15, 20, inf, 25],
#      [inf, 15, 0, 10, 20, inf],
#      [40, 20, 10, 0, 10, 25],
#      [25, inf, 20, 10, 0, 55],
#      [10, 25, inf, 25, 55, 0]]
# edges = []
# for i in range(1,7):
#     for j in range(i, 7):
#         edges.append((i, j, m[i-1][j-1]))

nodes = [0,1,2,3,4,5,6]
edges = [(0,1,1),(0,2,7),(1,0,3),(1,2,3),(1,4,1),(2,1,1),(2,5,5),(2,3,3),(3,4,1),(4,3,2),(5,2,2),(5,4,3),(5,6,2)]
graph = nx.DiGraph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)

res = nx.single_source_dijkstra(graph, source=0)
print(res)