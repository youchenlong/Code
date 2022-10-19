import networkx as nx
import matplotlib.pyplot as plt

nodes = [1, 2, 3, 4, 5, 6]
edges = [(1, 2, 3), (1, 4, 2), (2, 3, 1), (2, 4, 1), (2, 5, 7), (3, 4, 6), (3, 5, 1), (3, 6, 2), (4, 6, 5), (5, 6, 5)]
graph = nx.Graph()
graph.add_nodes_from(nodes)
graph.add_weighted_edges_from(edges)

def Dijkstra(graph, source):
    assert source in graph.nodes, 'source dose not exist in graph!'
    for node in graph.nodes:
        graph.nodes[node]['status'] = 'unvisited'
        graph.nodes[node]['distance'] = float('inf')
        graph.nodes[node]['parent'] = node
    graph.nodes[source]['distance'] = 0
    n = graph.number_of_nodes()
    for _ in range(n):
        u = 0
        minDistance = float('inf')
        for node in nodes:
            if graph.nodes[node]['status'] == 'unvisited' and graph.nodes[node]['distance'] < minDistance:
                u = node
                minDistance = graph.nodes[node]['distance']
        graph.nodes[u]['status'] = 'visited'
        for v in list(graph.adj[u]):
            if graph.nodes[v]['status'] == 'unvisited' and \
                    graph.nodes[u]['distance'] + graph[u][v]['weight'] < graph.nodes[v]['distance']:
                graph.nodes[v]['distance'] = graph.nodes[u]['distance'] + graph[u][v]['weight']
                graph.nodes[v]['parent'] = u

def BellmanFord(graph, source):
    assert source in graph.nodes, 'source dose not exist in graph!'
    for node in graph.nodes:
        graph.nodes[node]['distance'] = float('inf')
        graph.nodes[node]['parent'] = node
    graph.nodes[source]['distance'] = 0
    n = graph.number_of_nodes()
    for _ in range(n):
        for edge in graph.edges:
            u, v = edge
            if graph.nodes[u]['distance'] + graph[u][v]['weight'] < graph.nodes[v]['distance']:
                graph.nodes[v]['distance'] = graph.nodes[u]['distance'] + graph[u][v]['weight']
                graph.nodes[v]['parent'] = u

# Dijkstra(graph, 1)
# BellmanFord(graph, 1)

# nx.draw(graph, with_labels=True)
# plt.show()