#Energy Conservation via Domatic Partitions
#Implementation

#k-domatic partition problem

#ACRONYMS
# MIS = Maximal Independent Set
# Independent set = set of vertices such that [for every two verts, there is no edge connecting them]

#https://ieeexplore.ieee.org/document/7858445

import sys
import graphics as g
# import graph as gr
# global BLACK,WHITE,RED,GREEN,BLUE,rect,image,external_funcs,screen,clock,FPS

#it may be better to construct a k-domatic
#partition for k > 1
k=2
coordinators = []
small_dom_set = []
vertices=[[0,0],[100,100],[400,300],[200,210]]
edges=[[0,1],[0,2],[1,2],[1,2],[2,3]]
texts = ["0","1","2","3"]
text_size=18
vertex_width=2
edge_width=2
graph = {}
def construct_graph(edges):
	G = {}
	for e in edges:
		if e[0] not in G:
			G[e[0]] = []
		if e[1] not in G[e[0]]:	
			G[e[0]].append(e[1])
		if e[1] not in G:
			G[e[1]] = []
		if e[0] not in G[e[1]]:
			G[e[1]].append(e[0])

	return G

def get_distance(vid1, vid2, G, dist=None, visited=None):
#	cur_dist = 0
	# if dist < 0:
	# 	return dist
	if not visited: visited = []
	if not dist: dist=0
	visited.append(vid1)
	if vid1 in G:
		dist += 1
		for other in G[vid1]:
			#print(str(vid1)+":"+str(G[vid1]))
			if vid2 == other:
				return dist
		for other in G[vid1]:
			#print(vid1,vid2,other)
			if other not in visited:
				#print("Continuing with "+str(other))
				#print(G[other])
				return get_distance(other,vid2,G, dist, visited)
			
	return -1
def get_distance(vid1, vid2, G, dist=None, visited=None):
#	cur_dist = 0
	# if dist < 0:
	# 	return dist
	if not visited: visited = []
	if not dist: dist=0
	visited.append(vid1)
	if vid1 in G:
		
		for other in G[vid1]:
			if vid2 == other:
				return dist
		for other in G[vid1]:
			if other not in visited:
				return get_distance(other,vid2,G, dist, visited)
			
	return -1

def get_neighbors(vid, G, at_dist):
	neighbors = []
	# print(get_edges(G))
	for j in range(len(get_edges(G))):
		if vid != j:
			dist = get_distance(vid, j, G)
			# print("dist of "+str(vid)+", "+str(j)+ " = "+str(dist))
			if dist == at_dist:
				neighbors.append(j)
	return neighbors

def get_max_distance(G):
	maxDist = 0
	for v in G:
		for e in G:
			if e != v:
				dist = get_distance(e,v,G)
				if dist > maxDist:
					maxDist = dist
	return maxDist

def add_edge_to_graph(i, j, G):
	id1 = i
	id2 = j
	if id1 not in G:
		G[id1] = []
	G[id1].append(id2)

	if id2 not in G:
		G[id2] = []
	G[id2].append(id1)
	return G

def get_edges(G):
	edges = []
	visited_edges = []
	for key in G.keys():
		for li in G[key]:
			if [key,li] not in visited_edges or [li,key] not in visited_edges:
				edges.append([key,li])
				visited_edges.append([key,li])
				visited_edges.append([li,key])
	return edges


def find_edge(v1,v2, edges):
	for e in edges:
		if e[0] == v1:
			if e[1] == v2:
				return e
		elif e[1] == v1:
			if e[0] == v2:
				return e
	return None
def power_graph(vertices,edges, graph, power):
	for i in range(len(vertices)):
		for j in range(len(vertices)):
			if i != j:
				e = find_edge(i,j, edges)
				#ean den uparxei connection
				if e is None:
					dist = get_distance(i,j,graph)
					if dist == power:
						graph = add_edge_to_graph(i, j, graph)
	print(graph)
	return graph

def independent_set(G):
#    excluded = []
#    if startIdx in G:
#        neighbs = G[startIdx]
#        for nei in neighbs:
#            excluded.append(nei)
	neighbors = []

	for dist in [2]:
		for v in G:
			neighbors.append([v]+get_neighbors(v,G,dist))
	print(neighbors)
	return set.union(*[set(nei) for nei in neighbors])

def MIS(G, nodes=None):
	
	if not nodes:
		nodes = set([random.choice(nodes)])     # pick a random node
	else:
		nodes = set(nodes)
	# if not nodes.issubset(G):
	# 	raise nx.NetworkXUnfeasible("%s is not a subset of the nodes of G" % nodes)
	
	# All neighbors of nodes
	for v in G:
		print(v,get_neighbors(v,G,1))
	neighbors = set.union(*[set(get_neighbors(v,G, 1)) for v in G])
	print("Neighbors:"+str(neighbors))
	print("Nodes:"+str(nodes))
	if set.intersection(neighbors, nodes):
		print("%s is not an independent set of G" % nodes)
	
	indep_nodes = list(nodes)       # initial
	available_nodes = set(nodes.difference(neighbors.union(nodes))) # available_nodes = all nodes - (nodes + nodes' neighbors)
	print("available nodes:"+str(available_nodes))
	while available_nodes:
		# pick a random node from the available nodes
		node = random.choice(list(available_nodes))
		indep_nodes.append(node)
	
		available_nodes.difference_update(neighbors(node,G, 1) + [node])   # available_nodes = available_nodes - (node + node's neighbors)
	
	return indep_nodes

def indep_set(G):
	indep_nodes = []
	for v in G:
		bAdd = True
		for indep in indep_nodes:
			distance = get_distance(v,indep,G)
			if distance <2 :
				bAdd = False
		if bAdd:
			indep_nodes.append(v)
			indep_nodes = list(set(indep_nodes))
		for dist in range(2,get_max_distance(G)+1):
			neighbors = get_neighbors(v, G, dist)
			for nei in neighbors:
				if nei not in indep_nodes:
					bAdd = True
					for indep in indep_nodes:
						distance = get_distance(nei,indep,G)
						if distance <2	:
							bAdd = False
					if bAdd:
						indep_nodes.append(nei)
						indep_nodes = list(set(indep_nodes))
					
	return indep_nodes

graph = construct_graph(edges)
# print(graph)
# neighbors = get_neighbors(0,graph,1)
# print(neighbors)

# sys.exit()


#First step of 2-DP3 algorithm
#	->Compute an MIS I of G.
# indep_nodes = MIS(graph, [0,1,2,3])
# print("Independent nodes I:"+str(indep_nodes))
# print(get_neighbors(0,graph,1))
# sys.exit()


#Second step of 2-DP3 algorithm
#	->Let G 2 denote the square of the graph G. So G 2 has
#	vertex set V (G) and edge set E 2 = {{u, v} | u, v ∈
#	V (G) and d(u, v) ≤ 2}. Let H = G 2 [I]. This is the
#	subgraph of G 2 induced by I. Let L = Δ(H). Com-
#	pute a proper (L + 1)-vertex coloring of H. Denote this
#	coloring by χ.
# graph = power_graph(vertices,edges, graph, 2)
# edges = get_edges(graph)

# indepentent = independent_set(graph)
# print(indepentent)
# print("Max distance = "+str(get_max_distance(graph)))
# indep_nodes = indep_set(graph)
# print("indep_nodes = "+ str(indep_nodes))
print("Distance of 0 3 "+ str(get_distance(0,3,graph)))
#Compute vertex-coloring
pass

#Third step. Each node u ∈ V (G) − I sets a variable status u ←
#	available. Each node v ∈ I sets a variable status v ←
#	unavailable.
pass

#Fourth step. For each color r = 1, 2, . . . , L + 1 used by χ, repeat the
#	following steps.
#		(a) Each node u ∈ V (G) − I whose status is available,
#		broadcasts its ID, ID u , to neighbors.



#		(b) Each node v ∈ I colored r by χ receives an ID
#		from each available neighbor and constructs the set
#		C v = {ID u | u ∈ N (v) and status u = available}.


#		(c) Each node v ∈ I colored r by χ picks the smallest
#		δ 1 /(L + 1) IDs from C v and places these in S v .
#		Node v then broadcasts {ID v } ∪ S v to neighbors.
#		For this step, it is not necessary that node v know
#		δ 1 . It is sufficient for v to instead use the smallest
#		vertex degree in its neighborhood instead of δ 1



#		(d) Each node u ∈ V (G) − I, whose status is available,
#		may receive a set S of IDs from a neighbor in I.
#		Node u then checks if ID u ∈ S and if so u sets
#		status u ← unavailable and S u ← S.






#Fifth step. Each unavailable node v computes the rank r of ID v in
#	S v and colors itself r. Each available node colors itself
#	1. Let this coloring of vertices be denoted χ  . Note that
#	this vertex coloring need not be proper.


def func():
	for vert in vertices:
		g.pygame.draw.rect(g.image,g.WHITE,vert+[vertex_width,vertex_width])
	# for edge in edges:
		# g.pygame.draw.line(g.image,g.RED,vertices[edge[0]],vertices[edge[1]],edge_width)
	for edge in edges:
		# pass
		g.pygame.draw.line(g.image,g.RED,vertices[edge[0]],vertices[edge[1]],edge_width)
	for i in range(len(vertices)):
		g.text_to_screen(g.image,texts[i],vertices[i][0],vertices[i][1],size=text_size)

# Graphics
g.init_graphics(500,500)

g.add_loop_function(func)

g.display()
