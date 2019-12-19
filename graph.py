import random
import queue as q	

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
class Queue(object):
	def __init__(self, queue=None):
		if queue is None:
			self.queue = []
		else:
			self.queue = list(queue)
		self.parent = None
	def dequeue(self):
		return self.queue.pop(0)
	def enqueue(self, element):
		self.queue.append(element)
	def empty(self):
		if len(self.queue) == 0:
			return True
		return False

def graph_1_hop_neighbors(v, G):
	return G[v]

def graph_n_hop_beighbors(v,G,n):
	if n == 0:
		return G[v]
	for i in G[v]:
		return set(graph_n_hop_beighbors(i,G,n-1))-set([v])
	


def BFS(G,start_v, compare_func):
	Q = Queue()
	discovered = {}
	discovered[start_v] = True
	Q.enqueue(start_v)
	while Q.empty() == False:
		v = Q.dequeue()
		# if v is the goal:
		# 	return v
		d = compare_func(v,G,1)
		if d is not None:
			return d
		# for all edges from v to w in G.adjacentEdges(v) do
		# 	if w is not labeled as discovered:
		# 		label w as discovered
		# 		w.parent = v
		# 		Q.enqueue(w) 
		# for all edges from v to w in G.adjacentEdges(v) do
		neighbors = graph_1_hop_neighbors(v, G)
		for w in neighbors:
			if w in discovered:
				if discovered[w] == False:
					discovered[w] = True
					w.parent = v
					Q.enqueue(w)

def fn(v,G, value):
	if v in G:
		for item in G[v]:
			if item == value:
				print("FOUND "+ str(value))
				return (v,value)
	return None
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
vertices=[[0,0],[100,100],[400,300],[200,210]]
edges=[[0,1],[0,2],[1,2],[1,2],[2,3]]
G = construct_graph(edges)
print(G)
ret = BFS(G,0,compare_func=fn)
print(ret)

print(graph_n_hop_beighbors(0,G,2))