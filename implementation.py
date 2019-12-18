#Energy Conservation via Domatic Partitions
#Implementation

#k-domatic partition problem


#https://ieeexplore.ieee.org/document/7858445

import sys
import graphics as g
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

def neighbor(vid1, vid2, G, dist=0, visited=None):
#	cur_dist = 0
	# if dist < 0:
	# 	return dist
	if not visited: visited = []
	visited.append(vid1)
	if vid1 in G:
		for other in G[vid1]:
			print(str(vid1)+":"+str(G[vid1]))
			if vid2 == other:
				return dist
			else:
				print(vid1,vid2,other)
		dist += 1
		for other in G[vid1]:
			#print(vid1,vid2,other)
			if other not in visited:
				print("Continuing with "+str(other))
				print(G[other])
				return neighbor(other,vid2,G, dist, visited)
			else:
				print("aborting->" + str(other))
			continue

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

graph = construct_graph(edges)
print(graph)
print("distance between " + str(0) +","+ str(3) + ":" + str(neighbor(0,3,graph)))
print("distance between " + str(0) +","+ str(3) + ":" + str(neighbor(0,3,graph)))
# sys.exit()

def get_edges(G):
	edges = []
	visited_edges = []
	print(G.keys())
	for key in G.keys():
		print(G[0])
		for li in G[key]:
			if [key,li] not in visited_edges or [li,key] not in visited_edges:
				edges.append([key,li])
	return edges
edges = get_edges({0: [1, 2, 3], 1: [4, 5]}
)
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
					dist = neighbor(i,j,graph)
					if dist == power:
						graph = add_edge_to_graph(i, j, graph)
	print(graph)
	return graph
graph = power_graph(vertices,edges, graph, 2)
edges = get_edges(graph)
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
# func()
#Graphics
g.init_graphics(500,500)

g.add_loop_function(func)

g.display()
