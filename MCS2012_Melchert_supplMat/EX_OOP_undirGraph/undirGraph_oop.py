import sys


class myGraph(object):
	"""adjacency-list representation of an undirected simple graph G=(V,E)

	The graph consists of nNodes nodes. For each node n in V
	the adjacency list adjList(n) contains all other nodes u
	such that there is an edge {n,u} in E. Simple means that 
	there are no multiple edges between pairs of nodes and 
	there are no self-edges.

	"""
	def __init__(self):
		"""default constructor for a new instance of class myGraph"""
		
		self._nNodes=0	# number of nodes and edges (leading underscore means 
		self._nEdges=0	# these will be considered to be private attributes)
		
		self._adjList={}# ini unordered set of node:_adjList pairs 
				# data struct: dictionary

	
	@property
	def V(self): 
		"""returns node set of the graph"""
		return self._adjList.keys()

	@property
	def nNodes(self): 
		"""returns number of nodes in the graph"""
		return self._nNodes

	@nNodes.setter
	def nNodes(self,val): print "will not change private attribute"

	@property
	def nEdges(self): 
		"""returns number of edges in the graph"""
		return self._nEdges

	@nEdges.setter
	def nEdges(self,val):  print "will not change private attribute"

	def adjList(self,node):
		"""returns adjacency list of node"""
		return self._adjList[node]

	def deg(self,node):
		"""returns degree of node"""
		return len(self._adjList[node])

	def addNode(self,node):
		"""add node to graph and create empty adjacency list
		if node is new"""
		if node not in self.V: 
			self._adjList[node]=[]
			self._nNodes += 1

	def delNode(self,node):
		"""delete node and all its incident edges from the graph"""
		if node not in self.V: 
			sys.exit("ERROR in delNode(): node does not exist")
		# traverste adjacency list and delete node
		#for nb in [nbNodes for nbNodes in self._adjList[node]]:
		for nb in self.adjList(node):
			self.delEdge(nb,node)
		del self._adjList[node]
		self._nNodes -= 1

	def addEdge(self,fromNode,toNode):
		"""add edge to the graph and update adjacency lists
		of its terminal nodes. If terminal nodes do not 
		exist, create them first"""
		flag=0
		self.addNode(fromNode)
		self.addNode(toNode)
		#if (fromNode != toNode) and (toNode not in self._adjList[fromNode]):
		if (fromNode != toNode) and (toNode not in self.adjList(fromNode)):
			self._adjList[fromNode].append(toNode)
			self._adjList[toNode].append(fromNode)
			self._nEdges += 1
			flag=1
		return flag

	__addEdge=addEdge

	def delEdge(self,fromNode,toNode):
		"""delete edge from graph, i.e. modify adjacency lists
		of its terminal nodes"""
		flag=0
		if fromNode in self.adjList(toNode):
			self._adjList[fromNode].remove(toNode)
			self._adjList[toNode].remove(fromNode)
			self._nEdges -= 1
			flag=1
		return flag

	__delEdge=delEdge


	def __str__(self):
		"""print graph in graphviz format
		"""
		string  = 'graph G {\
		  \n  rankdir=LR;\
		  \n  node [shape = circle,size=0.5];\
		  \n  // graph attributes:\
		  \n  // nNodes=%d\
		  \n  // nEdges=%d\
		  \n'%(self.nNodes,self.nEdges)

		string += '\n  // node-list:\n'
		for n in self.V:
		  string += '  %s; // deg=%d\n'%\
					(str(n),self.deg(n))

		string += '\n  // edge-list:\n'
		for n1 in self.V:
		  for n2 in self.adjList(n1):
		    if n1<n2:
		      string += '  %s -- %s [len=1.5];\n'%\
					(str(n1),str(n2))
		string += '}'
		return string

	def oldStrRep(self):
		"""print graph in adjacency list representation to stdout"""
		string='# adjacency-list representation \n'
		string+='# nNodes=%d\n'%(self.nNodes)
		string+='# nEdges=%d\n'%(self.nEdges)
		string+='# node [deg]: adjList\n'
		for node in self.V:
			string+='%s [%d]: (%s)\n'%(str(node),self.deg(node),','.join(map(lambda x: str(x),self._adjList[node])))
		return string

class myWeightedGraph(myGraph):
	def __init__(self):
		myGraph.__init__(self)
		self._wgt={}

	@property
	def E(self): return self._wgt.keys()

	def wgt(self,fromNode,toNode):
		"""return the weight of the edge {fromNod,toNode}"""
		sortedEdge = (min(fromNode,toNode),max(fromNode,toNode))
		return self._wgt[sortedEdge]

	def setWgt(self,fromNode,toNode,wgt):
		"""set the weight of the edge {fromNod,toNode}"""
		if toNode in self.adjList(fromNode):
			sortedEdge = (min(fromNode,toNode),max(fromNode,toNode))
			self._wgt[sortedEdge]=wgt

	def addEdge(self,fromNode,toNode,wgt=1):
		"""add weighted edge to the graph and update adjacency lists
		of its terminal nodes. If terminal nodes do not 
		exist, create them first"""
		if self._myGraph__addEdge(fromNode,toNode):
			self.setWgt(fromNode,toNode,wgt)

	def delEdge(self,fromNode,toNode):
		"""delete edge from graph, i.e. modify adjacency lists
		of its terminal nodes"""
		if self._myGraph__delEdge(fromNode,toNode):
			sortedEdge = (min(fromNode,toNode),max(fromNode,toNode))
			del self._wgt[sortedEdge]


	def __str__(self):
		"""print graph in graphviz format
		"""
		string  = 'graph G {\
		  \n  rankdir=LR;\
		  \n  node [shape = circle,size=0.5];\
		  \n  // graph attributes:\
		  \n  // nNodes=%d\
		  \n  // nEdges=%d\
		  \n'%(self.nNodes,self.nEdges)

		string += '\n  // node-list:\n'
		for n in self.V:
		  string += '  %s; // deg=%d\n'%\
					(str(n),self.deg(n))

		string += '\n  // edge-list:\n'
		for n1 in self.V:
		  for n2 in self.adjList(n1):
		    if n1<n2:
		      string += '  %s -- %s [label=%lf,len=1.5];\n'%\
					(str(n1),str(n2),self.wgt(n1,n2))
		string += '}'
		return string



class hypercubicLattice(myGraph):

	def __init__(self,d,lList):
		myGraph.__init__(self)
		self.d=d
		self.L=lList
		self.setNodes()

	def _product(self,a):
		result=1
		for val in a: result*=val
		return result

	def _int2tuple(self,myInt):
		return tuple((myInt/self._product(self.L[:d]))%self.L[d] for d in range(self.d) )

	def setNodes(self):
		"""initialize nodes on hypercubic lattice graph in d dimension
		for given side lengths"""
		# overall number of nodes in graph
		nNodes=self._product(self.L)

		# add lattice points to node set 
		for nId in range(nNodes):
			# transform integer node id to d-tuple, representing
			# a lattice point in d-dimensional space
			coord = self._int2tuple(nId)
			self.addNode(coord)

	def nearestNeighbors(self):
		"""fill adjacency lists for nodes on hypercubic lattice graph in d dimensions"""
		# fill adjacency lists
		for coord in self.V:
			for di in range(self.d):
				for diff in [-1,+1]:
					coordList=list(coord)
					coordList[di] = (coordList[di]+diff)%self.L[di]
					neighborCoord = tuple(coordList)
					self.addEdge(coord,neighborCoord)

	
	
def breadthFirstSearch(G,s):
	color={}; dist={}; pre={}

	for u in G.V:
		color[u]=0
		dist[u]=None
		pre[u]=None

	color[s]=1; dist[s]=0; pre[s]=None

	Q=[s]
	while Q:
	  u=Q.pop()
	  for v in G._adjList[u]:
	    if color[v]==0:
		color[v]=1
		dist[v]=dist[u]+1
		pre[v]=u
		Q.append(v)
	  color[u]=2

	return dist,pre

	
def printPath_helper(pre,s,v):
	if s==v: print s,
	else: 
	  	 printPath_helper(pre,s,pre[v])
		 print v,


def printPaths(g,dist,pre,s):
	print '# list distances and paths to all nodes reachable from node %d'%(s)
	for u in g.V:
	  if u!=s and dist[u]!=None:
	    print 'dist(%d,%d)= %d \t path(%d,%d)=('%(s,u,dist[u],s,u),
	    printPath_helper(pre,s,u)
	    print ')'


def exampleGraph():
	g = myGraph()

	g.addEdge(1,2)
	g.addEdge(1,4)
	g.addEdge(2,5)
	g.addEdge(3,5)
	g.addEdge(3,6)
	g.addEdge(4,2)
	g.addEdge(5,4)
	g.addEdge(5,6)

	return g

def main():
	g = exampleGraph()

	print g
	print

	dist,pre = breadthFirstSearch(g,1)
	printPaths(g,dist,pre,1)

if __name__=="__main__":
   main()
