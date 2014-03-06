## \file   MCS2012_mstKruskal.py
#  \brief  implementation of Kruskals minimum weight
#          spanning tree algorithm using a union
#          find data structure
#
#  \author OM
#  \date   12.06.2012

class unionFind_cls:
	"""union find data structure that implemnts
	union-by-size
	"""
	def __init__(self):
		self.nSets = 0
                self.root  = dict()
                self.size  = dict()
                self.mySet = dict()

        def makeSet(self,i):
                self.mySet[i]=set()
                self.mySet[i].add(i)
                self.root[i] = i
                self.size[i] = 1
                self.nSets  += 1

	def find(self,i):
		while(i!=self.root[i]):
			i = self.root[i]
		return i
		
	def union(self,i,j):
		if self.size[i]<self.size[j]:
			dum = i; i=j; j=dum

		self.root[j] =i
		self.size[i]+= self.size[j]
		self.size[j] =0
		self.nSets  -=1
		self.mySet[i].union(self.mySet[j])
		del self.mySet[j]

def mstKruskal(G):
	"""Kruskals minimum spanning tree algorithm 
        
        algorithm for computing a minimum spanning 
        tree T=(V,E') for a connected, undirected and weighted 
        graph G=(V,E,w) as explained in 
        'Introduction to Algorithms', 
        Cormen, Leiserson, Rivest, Stein, 
        Chapter 23.2 on 'The algorithms of Kruskal and Prim'
	
	Input:
	G       - weighted graph data structure

	Returns: (T,wgt)
	T       - minimum spanning tree stored as edge list
        wgt     - weight of minimum weight spanning tree
	"""
	uf = unionFind_cls()
	T=[]
        K = sorted(G.E,cmp=lambda e1,e2: cmp(G.wgt(e1),G.wgt(e2)))

        for i in G.V:
	        uf.makeSet(i)

	for (v,w) in K:
		if uf.find(v)!=uf.find(w):
			uf.union(uf.find(v),uf.find(w))
			T.append((v,w))

        return T, sum(map(lambda e: G.wgt(e),T))


def mstGraphviz(G,T):
        """print graph in graphviz format
        """
        string  = 'graph G {\
          \n  rankdir=LR;\
          \n  node [shape = circle,size=0.5];\
          \n  // graph attributes:\
          \n  // nNodes=%d\
          \n  // nEdges=%d\
          \n'%(G.nNodes,G.nEdges)

        string += '\n  // node-list:\n'
        for n in G.V:
          string += '  %s; // deg=%d\n'%\
                                (str(n),G.deg(n))

        string += '\n  // edge-list:\n'
        for n1 in G.V:
          for n2 in G.adjList(n1):
            if n1<n2:
              myStyle="setlinewidth(3)"; myColor='grey'
              if tuple(sorted([n1,n2])) in T: myStyle="setlinewidth(6)"; myColor='black'
              string += '  %s -- %s [style=\"%s\",label=%d,len=1.5,color=\"%s\"];\n'%\
                                (str(n1),str(n2),myStyle,int(G.wgt((n1,n2))),myColor)
        string += '}'
        return string

# EOF: MCS2012_mstKruskal.py
