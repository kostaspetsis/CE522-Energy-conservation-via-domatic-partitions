import networkx as nx


def construct_graph(vertices,edges):
	G = nx.Graph()
	nxedges=[]
	nxnodes=[]
	for e in edges:
		nxedges.append((e[0],e[1]))
	for v in range(len(vertices)):
		nxnodes.append(v)
	G.add_nodes_from(nxnodes)
	G.add_edges_from([nxe for nxe in nxedges])
	return G

def shortest_distance(G, node1, node2):
	return nx.dijkstra_path_length(G,node1,node2)

def MIS(G):
	return nx.maximal_independent_set(G)

def adjacent(G,node):
	return list(G.neighbors(node))

def find_edge(G,i,j):
	_edges = list(G.edges(i))
	for _e in _edges:
		if _e[1] == j:
			return (_e[0],_e[1])
	return None

def power_graph(G, vertices, power):
	for i in range(len(vertices)):
		for j in range(len(vertices)):
			if i != j:
				e = find_edge(G,i,j)
				#ean den uparxei connection
				if e is None:
					dist = shortest_distance(G, i,j)
					if dist == power:
						G.add_edge(i,j)
	
	return G


def serialize(G):
	print("Edges:"+str(G.edges()))
	print("Nodes:"+str(G.nodes()))

messages = []
def broadcast(node, id, toOtherNodesList):
	for other in toOtherNodesList:
		messages.append("Broadcast From:"+"Node["+str(node)+"],id["+str(id)+"] To ->id["+str(other)+"]")

vertices=[[0,0],[100,100],[400,300],[200,210]]
vertices_ID=[id for id in range(len(vertices))]
edges=[[0,1],[0,2],[1,2],[1,2],[2,3]]

G=construct_graph(vertices,edges)
print(G.edges())


print(adjacent(G,0))
print(adjacent(G,1))
print(adjacent(G,2))
print(adjacent(G,3))
print(G.graph)
# print(find_edge(G,0,3))

#Step 1-MIS
independent_set = set(MIS(G))
print("Independent set :" + str(independent_set))


#Step 2-G=G^2
G = power_graph(G, vertices, 2)
serialize(G)

#Step 3-u ∈ V (G) − I sets a variable status u available.
# Each node v ∈ I sets a variable status v ← unavailable.
available = set([i for i in range(len(vertices))]).difference(independent_set)
unavailable = independent_set

#Fourth step. For each color r = 1, 2, . . . , L + 1 used by χ, repeat the
#	following steps.
colors = [1]#????????
for c in colors:

#	(a) Each node u ∈ V (G) − I whose status is available,
#	broadcasts its ID, ID u , to neighbors.
	for v in available:
		broadcast(v,vertices_ID[v], adjacent(G,v))
	print(messages)

#	(b) Each node v ∈ I colored r by χ receives an ID
#	from each available neighbor and constructs the set
#	C v = {ID u | u ∈ N (v) and status u = available}.


