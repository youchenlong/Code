import networkx as nx
import matplotlib.pyplot as plt

nodes = ['A','B','C','D','E']
edges = [('A','B',10),('B','D',5),('A','D',20),('A','C',3),('C','E',15),('C','B',2),('D','E',11)]
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)
# 基本概念
graph.degree['A']
graph.adj['A']
# 最短路径
nx.dijkstra_path(graph, 'A', 'B')
nx.dijkstra_path_length(graph, 'A', 'B')
nx.bellman_ford_path(graph, 'A', 'B')
nx.bellman_ford_path_length(graph, 'A', 'B')
nx.floyd_warshall(graph)
nx.floyd_warshall_numpy(graph)
# 最小生成树
nx.minimum_spanning_tree(graph, algorithm='kruskal')
nx.minimum_spanning_tree(graph, algorithm='prim')
# 绘图
nx.draw(graph, with_labels=True)
plt.show()