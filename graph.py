import random
	
def MIS(G, nodes=None):
	
	if not nodes:
		nodes = set([random.choice(nodes)])     # pick a random node
	else:
		nodes = set(nodes)
	# if not nodes.issubset(G):
	# 	raise nx.NetworkXUnfeasible("%s is not a subset of the nodes of G" % nodes)
	
	# All neighbors of nodes
	neighbors = set.union(*[set(neighbors(0,G, 1)) for v in nodes])
	if set.intersection(neighbors, nodes):
		raise nx.NetworkXUnfeasible("%s is not an independent set of G" % nodes)
	
	indep_nodes = list(nodes)       # initial
	available_nodes = set(nodes.difference(neighbors.union(nodes))) # available_nodes = all nodes - (nodes + nodes' neighbors)
	print(available_nodes)
	while available_nodes:
		# pick a random node from the available nodes
		node = random.choice(list(available_nodes))
		indep_nodes.append(node)
	
		available_nodes.difference_update(neighbors(node,G, 1) + [node])   # available_nodes = available_nodes - (node + node's neighbors)
	
	return indep_nodes
# MIS(nx.Graph())