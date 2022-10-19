import networkx as nx
import matplotlib.pyplot as plt

edges = [(1,2),(1,3),(2,4),(2,5),(3,6),(3,7),(4,8),(5,8),(6,8),(7,8)]
graph = nx.Graph(edges)

def dfs(graph, source):
    assert source in graph.nodes, 'source dose not exist in graph!'
    openset = []
    closeset = []
    for node in graph.nodes:
        graph.nodes[node]['status'] = 'unvisited'
    openset.append(source)
    while openset:
        E = openset.pop()
        if graph.nodes[E]['status'] != 'visited':
            closeset.append(E)
            graph.nodes[E]['status'] = 'visited'
            for node in list(graph.adj[E])[::-1]:
                if graph.nodes[node]['status'] == 'unvisited':
                    openset.append(node)
    return closeset

def bfs(graph, source):
    assert source in graph.nodes, 'source dose not exist in graph!'
    openset = []
    closeset = []
    for node in graph.nodes:
        graph.nodes[node]['status'] = 'undetected'
    openset.append(source)
    graph.nodes[source]['status'] = 'unvisited'
    while openset:
        E = openset.pop(0)
        if graph.nodes[E]['status'] != 'visited':
            closeset.append(E)
            graph.nodes[E]['status'] = 'visited'
            for node in graph.adj[E]:
                if graph.nodes[node]['status'] == 'undetected':
                    openset.append(node)
                    graph.nodes[node]['status'] = 'unvisited'
    return closeset

print(dfs(graph, 1))
print(bfs(graph, 1))
plt.show()