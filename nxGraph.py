import networkx as nx
import matplotlib.pyplot as plt

import sys
import equitable_color as coloring

def construct_graph(vertices,edges):
	G = nx.Graph()
	nxedges=[]
	nxnodes=[]
	for e in edges:
		nxedges.append((e[0],e[1]))
	# for v in range(len(vertices)):
	# 	nxnodes.append(v)
	for v in vertices:
		nxnodes.append(v)
	G.add_nodes_from(nxnodes)
	G.add_edges_from([nxe for nxe in nxedges])
	# print(G.edges())
	# sys.exit()
	return G

def shortest_distance(G, node1, node2):
	return nx.dijkstra_path_length(G,node1,node2)

def MIS(G):
	#return [8, 0, 3, 6]

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
	# for i in range(len(vertices)):
	# 	for j in range(len(vertices)):
	# 		if i != j:
	# 			e = find_edge(G,i,j)
	# 			#ean den uparxei connection
	# 			if e is None:
	# 				dist = shortest_distance(G, i,j)
	# 				if dist == power:
	# 					G.add_edge(i,j)
	return nx.power(G,power)
	return G


def serialize(G):
	print("Edges:"+str(G.edges()))
	print("Nodes:"+str(G.nodes()))

def n_min(list1,n): 
	t=[]
	list1copy = list1.copy()
	for i in range(n):
		t.append(min(list1copy))#append min of list in a new list
		list1copy.remove(min(list1copy))#remove min of list from the list
	print('by n_min function: ',t)
	return t
messages = []
b_messages = {}
def broadcast(node, id, toOtherNodesList):
	for other in toOtherNodesList:
		messages.append("Broadcast From:"+"Node["+str(node)+"],id["+str(id)+"] To ->id["+str(other)+"]")
		if other not in b_messages:
			b_messages[other] = []
		b_messages[other].append(id)
# vertices=[[0,0],[100,100],[400,300],[200,210]]
# vertices_ID=[id for id in range(len(vertices))]
# edges=[[0,1],[0,2],[1,2],[2,3]]

edges=[[1,2],
[2,3],
[1,3],
[1,9],
[1,3],
[9,8],
[4,3],
[4,6],
[4,5],
[6,5],
[6,7],
[7,8],
[7,3],
[0,1]
]
vertices=[i for i in range(0,9)]
vertices_ID=[id for id in range(len(vertices))]

G=construct_graph(vertices,edges)
# G=nx.graph_atlas()
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
pos=nx.spring_layout(G)
G2 = power_graph(G, vertices, 2)


G2_edges = []
for node in list(independent_set):
	for e in G2.edges():
		if e[0] == node and e[1] in list(independent_set):
			G2_edges.append(e)
			break
		elif e[1] == node and e[0] in list(independent_set):
			G2_edges.append(e)
			break
H = nx.Graph()
H.add_nodes_from(list(independent_set))
H.add_edges_from(G2_edges)
L=max([H.degree(i) for i in H.nodes()])
print("L=Δ(H)="+str(L))
# d = nx.coloring.greedy_color(H, strategy=nx.coloring.strategy_independent_set)
id_color_map = coloring.equitable_color(H,num_colors=L+1)
print(id_color_map)
print("dasdasd")
colors = {}
for k  in id_color_map:
	if id_color_map[k] not in colors :
		colors[id_color_map[k]] = []
	colors[id_color_map[k]].append(k)
print (colors)
# nx.draw_networkx_nodes(H,pos,
#                        nodelist=H.nodes(),
#                        node_color='g',
#                        node_size=500,
#                    alpha=0.8)
nx.draw_networkx_nodes(H,pos,
					   nodelist=id_color_map.keys(),
					   node_color=[col for col in id_color_map.values()],
					   node_size=500,
				   alpha=0.8)
nx.draw_networkx_edges(H,pos,
					   edgelist=H.edges(),
					   width=8,alpha=0.5,edge_color='g')
labels = {id_color_map: id_color_map for id_color_map in H.nodes}
nx.draw_networkx_labels(H, pos, labels, font_size=16, font_color='black')
#	Compute a proper (L + 1)-vertex coloring of H. Denote this
#	coloring by χ
# d=nx.algorithms.coloring.greedy_color(G2)


#Step 3-u ∈ V (G) − I sets a variable status u available.
# Each node v ∈ I sets a variable status v ← unavailable.
available = set([i for i in range(len(vertices))]).difference(independent_set)
G_Except_I = available
unavailable = independent_set

#Fourth step. For each color r = 1, 2, . . . , L + 1 used by χ, repeat the
#	following steps.
# colors = x
# print(colors)
S = {}
for c in colors:

#	(a) Each node u ∈ V (G) − I whose status is available,
#	broadcasts its ID, ID u , to neighbors.
	for v in available:
		broadcast(v,vertices_ID[v], adjacent(G,v))
	print(messages)

#	(b) Each node v ∈ I colored r by χ receives an ID
#	from each available neighbor and constructs the set
#	C v = {ID u | u ∈ N (v) and status u = available}.
	Cu = []
	for node in list(independent_set):
		# if c[node] == c:
		if id_color_map[node] == c:
			neighbors = adjacent(G,node)
			
			for n in neighbors:
				if n in available:
					Cu.append(n)

#	Each node v ∈ I colored r by χ picks the smallest
#	δ 1 /(L + 1) IDs from C v and places these in S v .
#	Node v then broadcasts {ID v } ∪ S v to neighbors.
#	For this step, it is not necessary that node v know
#	δ 1 . It is sufficient for v to instead use the smallest
#	vertex degree in its neighborhood instead of δ 1 .
	# Su = []
	# for node in list(independent_set):	
	# 	if id_color_map[node] == c:
			if node not in S:
				S[node] = []
			d1 = min([G.degree(i) for i in neighbors])
			numOfSmallest = d1/(L+1)
			smallests = n_min(Cu,numOfSmallest)
			for small in smallests:
				S[node].append(small)

#	(d) Each node u ∈ V (G) − I, whose status is available,
#	may receive a set S of IDs from a neighbor in I.
#	Node u then checks if ID u ∈ S and if so u sets
#	status u ← unavailable and S u ← S.			
	for node in G_Except_I:
		if node in available:
			neighbors = adjacent(G,node)
			neighbors = set(neighbors)
			neighbors_in_I = neighbors.intersection(independent_set)
			# get_random_neighbor
			nei = random.choice(neighbors_in_I)
			# get the set S from the previous neighbor
			set_S = S[nei]
			if node in set_S:#if IDu belongs to previous set S
				#get removed from available
				available.remove(node)
				#sets status to unavailable
				unavailable.add(node)

				#Su <- S???????
				# TODO
				# Isws S[node] = set_S

#5] Each unavailable node v computes the rank r of ID v in
#S v and colors itself r. Each available node colors itself
#1. Let this coloring of vertices be denoted x' . Note that
#this vertex coloring need not be proper.




# nx.draw_networkx(G)

# plt.axis('off')
# plt.show()
# nx.draw_networkx(G2)
# plt.show()

# plt.plot()

plt.figure()
nx.draw_networkx(G)
plt.plot()


plt.figure()
nx.draw_networkx(G2)
plt.plot()

plt.show() # only do this once, at the end