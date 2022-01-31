from collections import defaultdict 

class Vertex:
	def __init__(self, n):
		self.name = n
		self.neighbors = list()
		
		self.discovery = 0
		self.finish = 0
		self.color = 'black'
		
	
	def add_neighbor(self, v):
		if v not in self.neighbors:
			self.neighbors.append(v)
			self.neighbors.sort()

class Graph:



	vertices = {}
	
	
	def add_vertex(self, vertex):
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
			self.vertices[vertex.name] = vertex
			return True
		else:
			return False
	
	def add_edge(self, u, v):
		if u in self.vertices and v in self.vertices:
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
			
	def get_dic(self):
		map_dict={}
		
		for key in sorted(list(self.vertices.keys())):
			map_dict[key]=(self.vertices[key].neighbors)

		return map_dict

			
		
		
	def print_graph(self):
		
		for key in sorted(list(self.vertices.keys())):

			print(key + str(self.vertices[key].neighbors) + "  " )
		



	# def is_reachable(self,start,end):
	# 	vertex_num=len(self.vertices)

	# 	# vertex_list=list(self.vertices.keys())
	# 	# print(vertex_list)
	# 	visited =[False]*(vertex_num)
	# 	queue=[]
	# 	queue.append(start)
	# 	vertex_list=list(self.graph.keys())
	# 	print(vertex_list)
	# 	c=vertex_list.index(start)
	# 	visited[c] = True
	# 	while queue:
	# 		n = queue.pop(0)
	# 		if n == end:
	# 			return True
	# 		for i in self.graph[n]:
	# 			if visited[vertex_list.index(i)] == False:
	# 				queue.append(i)
	# 				visited[vertex_list.index(i)] = True
	# 	return False

		# start_index =list(self.vertices.keys()).index(start)
		# queue.append(start_index)
		# visited[start_index] = True
		# while queue:
		# 	n = queue.pop(0)
		# 	print(n)
		# 	if n == end:
		# 		return True
		# 	for i in self.graph[n]:
		# 		if visited[i] == False:
		# 			queue.append(i)
		# 			visited[i] = True
		# return False

			


	# def _dfs(self, vertex):
	# 	travel_list=[]
	# 	vertex.color = 'red'
	# 	for v in vertex.neighbors:
	# 		if self.vertices[v].color == 'black':
	# 			self._dfs(self.vertices[v])
	# 	vertex.color = 'blue'
		
	# def dfs(self, vertex):
	# 	self._dfs(vertex)
		
	



				

			
			
# g = Graph()




# for i in range(ord('A'), ord('K')):
# 	g.add_vertex(Vertex(chr(i)))

# edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
# for edge in edges:
# 	g.add_edge(edge[:1], edge[1:])

# start =Vertex('A'); end = Vertex('B')
# g.add_vertex(start)
# g.add_vertex(end)

# start='A'; end='B'




# map_dic=g.get_dic()
# print(map_dic['A'][0])
# print(g.vertices.keys())
# g.dfs('A')
# g.print_graph()