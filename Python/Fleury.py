"""
Fleury算法：除非没有选择，否则不走割边
割边判断：去掉该边后的生成子图连通分支数增加
networkx: subgraph_view + number_connected_components
"""

import networkx as nx

def Fleury(graph):
    assert nx.is_eulerian(graph), 'graph is not Euler graph'
    cycles = []
    for e in graph.edges:
        graph.edges[e]['status'] = 'unvisited'
    def filter_edge(u, v):
        # 边的导出子图的条件
        return graph[u][v]['status'] == 'unvisited'
    def choose(subgraph, u):
        # 返回选择的边
        for v in subgraph.adj[u]:
            graph[u][v]['status'] = 'visited'
            if nx.number_connected_components(subgraph) > 1:
                return v
            else:
                graph[u][v]['status'] = 'unvisited'
        v = list(subgraph.adj[u])[0]
        graph[u][v]['status'] = 'visited'
        return v
    def union(cycles):
        if len(cycles) == 1:
            return cycles[0]
        euler_cycle = cycles[0]
        for cycle in cycles[1:]:
            if len(cycle) > 1:
                i = euler_cycle.index(cycle[0])
                euler_cycle = euler_cycle[:i+1] + cycle[1:] + euler_cycle[i+1:]
        return euler_cycle
    subgraph = nx.subgraph_view(graph, filter_edge=filter_edge)
    for u in graph.nodes:
        cycle = [u]
        while subgraph.degree[u] > 0:
            v = choose(subgraph, u)
            cycle.append(v)
            u = v
        cycles.append(cycle)
    euler_cycle = union(cycles)
    return euler_cycle

edges = [(1, 2), (1, 3), (1, 5), (1, 6), (2, 3), (2, 4), (2, 5), (3, 4), (3, 6), (4, 5), (4, 6), (5, 6)]
graph = nx.Graph(edges)
print(Fleury(graph))