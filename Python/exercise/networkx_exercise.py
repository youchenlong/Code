import networkx as nx
import matplotlib.pyplot as plt

nodes = ['A','B','C','D','E']
edges = [('A','B',10),('B','D',5),('A','D',20),('A','C',3),('C','E',15),('C','B',2),('D','E',11)]
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)
# 最短路径
print(nx.dijkstra_path(graph, 'A', 'B'))
print(nx.dijkstra_path_length(graph, 'A', 'B'))
print(nx.bellman_ford_path(graph, 'A', 'B'))
print(nx.bellman_ford_path_length(graph, 'A', 'B'))
print(nx.floyd_warshall(graph))
print(nx.floyd_warshall_numpy(graph))


nodes = ['A','B','C','D','E','F']
edges = [('A','C',7),('A','E',9),('C','B',5),('C','D',1),('C','F',2),('B','F',6),('D','F',2),('E','F',1)]
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)
# 最小生成树
mst = nx.minimum_spanning_tree(graph, algorithm='kruskal')
# mst = nx.minimum_spanning_tree(graph, algorithm='prim')
nx.draw(mst, with_labels=True)
plt.show()
