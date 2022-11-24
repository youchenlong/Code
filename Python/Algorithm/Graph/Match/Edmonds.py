import networkx as nx

G = nx.Graph()
G.add_weighted_edges_from({
    ('x1', 'y1', 99), ('x1', 'y2', 6), ('x1', 'y3', 59), ('x1', 'y4', 73),
    ('x2', 'y1', 79), ('x2', 'y2', 15), ('x2', 'y3', 93), ('x2', 'y4', 87),
    ('x3', 'y1', 67), ('x3', 'y2', 93), ('x3', 'y3', 13), ('x3', 'y4', 81),
    ('x4', 'y1', 16), ('x4', 'y2', 79), ('x4', 'y3', 66), ('x4', 'y4', 26)
})
print(sorted(nx.max_weight_matching(G)))