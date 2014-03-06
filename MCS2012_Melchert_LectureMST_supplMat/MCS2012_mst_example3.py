import sys
from MCS2012_scaleFreeGraph import scaleFreeGraph
from MCS2012_mstKruskal     import mstKruskal

def setWgt(G,wgtType):
        if wgtType == 1:
                for (i,j) in G.E:
                  G.setWgt((i,j), G.deg(i)*G.deg(j))
        if wgtType == 4:
                for (i,j) in G.E:
                  G.setWgt((i,j), 1./G.deg(i)*G.deg(j))
        return G

def mstGraphviz_tuneNodeSize(G,T):
        """print graph in graphviz format
        """
        string  = 'graph G {\
          \n  rankdir=LR;\
          \n  // graph attributes:\
          \n  // nNodes=%d\
          \n  // nEdges=%d\
          \n'%(G.nNodes,G.nEdges)

        degDict = dict((n,G.deg(n)) for n in G.V)
        maxDeg,minDeg  = max(degDict.values()),min(degDict.values())

        string += '\n  // node-list:\n'
        for n,deg in degDict.iteritems():
          mySize =  0.5 + (float(deg - minDeg)/(maxDeg-minDeg) )*(3.5)
          string += '  %s [shape=point, width=%lf,height=%lf,fixedsize=true]; // deg=%d\n'%\
                                (str(n),mySize,mySize,G.deg(n))

        string += '\n  // edge-list:\n'
        for n1,n2 in T:
              string += '  %s -- %s [len=1.5];\n'%(str(n1),str(n2))
        string += '}'
        return string

def main():
        N = 500       # number of nodes in graph
        m = 2           # numbers of neighbors added per time-step
        s = 1           # seed for growint the graph
        wgtType = 4     # type of weight distribution

        # prepare files for simulated data
        baseName = "wgtType%d_N%d_m%d_seed%d.dot"%(wgtType,N,m,s)
        outFile  = open("graph_"+baseName,'w')

        G = scaleFreeGraph(N,m,s)
        G = setWgt(G,wgtType)
        T,Twgt = mstKruskal(G)

        graphAsString = mstGraphviz_tuneNodeSize(G,T)
        outFile.write('%s'%(graphAsString))
        

main()
