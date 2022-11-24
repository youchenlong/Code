import networkx as nx
from networkx.algorithms import approximation as approx

G = nx.Graph()
G.add_weighted_edges_from({
    (1,2,13), (1,3,9), (1,4,6), (1,5,12), (2,3,15), (2,4,11), (2,5,10), (3,4,8), (3,5,7), (4,5,14)
})
cycle = approx.christofides(G)
cost = sum(G[n][nbr]["weight"] for n, nbr in nx.utils.pairwise(cycle))
print(cost)