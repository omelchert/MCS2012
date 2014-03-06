## \file   MCS2012_scaleFreeGraph.py
#  \brief  implementation of scale free graph
#          using preferential attachment
#
#  \author OM
#  \date   14.06.2012
import random
from MCS2012_uGraphWeighted import uGraphWeighted

seed    = random.seed
randInt = random.randint

def scaleFreeGraph(N,m,mySeed=0):
        seed(mySeed)
        G = uGraphWeighted()
        M = [0]*(2*N*m-m*(m+1))
        nPick = 0

        # use complete m-node graph as seed graph
        for i in range(m+1):
          for j in range(i+1,m+1):
                G.addEdge(i,j)
                M[nPick]   = i
                M[nPick+1] = j
                nPick +=2

        # construct graph by preferential attachment
        for i in range(m+1,N):
           G.addNode(i)
           t=0
           while(t<m):
                j = M[randInt(0,nPick)]
                if (i!=j) and (j not in G.adjList(i)):
                  G.addEdge(i,j)
                  M[nPick] = i
                  M[nPick+1] = j
                  nPick+=2
                  t+=1

        del M
        return G

# EOF: MCS2012_scaleFreeGraph.py
