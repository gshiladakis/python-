import networkx as nx
import matplotlib.pyplot as plt

# Generate a random groph
p = dict((i, (np.random.uniform(0, 1), np.random.uniform(0, 1)))
          for i in range(200))
g = nx.random_geometric_graph(200, 0.12, pos = p)
pos = nx.get_node_attribute(g, 'pos')

# Find node nearest the center point (0.5, 0.5)
dists = [ (x - 0.5) ** 2 + (y - 0.5) ** 2 for x, y in list (pos.values())]
ncenter = np.argmin(dists)

# Plot graph, coloring by path length from central node
p = nx.single_source_path_length(g, ncenter)
plt.figure()
nx.draw_networkx_edges(g, pos, alpha = 0.4)
nx.draw_network_nodes(g,
                      pos,
                      nodelist = list(p.keys()),
                      node_size = 120, alpha = 0.5,
                      node_color = list(p.values()),
                      cmap = plt.cm.jet_r)
plt.show()
