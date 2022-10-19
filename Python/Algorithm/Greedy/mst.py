import networkx as nx
import matplotlib.pyplot as plt
from UnionFind import UnionFind

nodes = [1, 2, 3, 4, 5, 6]
edges = [(1, 2, 3), (1, 4, 2), (2, 3, 1), (2, 4, 1), (2, 5, 7), (3, 4, 6), (3, 5, 1), (3, 6, 2), (4, 6, 5), (5, 6, 5)]
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)


def Kruskal(graph):
    mst = []
    unionfind = UnionFind(graph.number_of_nodes())
    edges = sorted(graph.edges(data=True), key=lambda e: e[2]['weight'])
    for edge in edges:
        p, q = edge[0] - 1, edge[1] - 1
        if not unionfind.is_connected(p, q):
            unionfind.union(p, q)
            mst.append(edge)
    return mst


def Prim(graph):
    mst = []
    select = list(graph.nodes)[:1]
    candidate = list(graph.nodes)[1:]
    n = graph.number_of_nodes()
    for _ in range(n - 1):
        u, v, min_weight = 0, 0, float('inf')
        for i in select:
            for j in candidate:
                if graph.has_edge(i, j) and graph[i][j]['weight'] < min_weight:
                    u, v, min_weight = i, j, graph[i][j]['weight']
        mst.append((u, v, ('weight', min_weight)))
        select.append(v)
        candidate.remove(v)
    return mst


mst = Kruskal(graph)
mst = Prim(graph)

nx.draw(graph, with_labels=True)
plt.show()
