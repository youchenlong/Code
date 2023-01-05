import networkx as nx

G = nx.Graph()
G.add_weighted_edges_from({
    ('x1', 'y1', 0), ('x1', 'y2', 93), ('x1', 'y3', 40), ('x1', 'y4', 26),
    ('x2', 'y1', 20), ('x2', 'y2', 84), ('x2', 'y3', 6), ('x2', 'y4', 12),
    ('x3', 'y1', 32), ('x3', 'y2', 6), ('x3', 'y3', 86), ('x3', 'y4', 18),
    ('x4', 'y1', 83), ('x4', 'y2', 20), ('x4', 'y3', 33), ('x4', 'y4', 73)
})
print(sorted(nx.max_weight_matching(G)))