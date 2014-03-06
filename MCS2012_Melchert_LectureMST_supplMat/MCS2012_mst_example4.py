import sys
from MCS2012_scaleFreeGraph import scaleFreeGraph
from MCS2012_mstKruskal     import mstKruskal
from MCS2012_lib            import basicStatistics
from math import sqrt

def setWgt(G,wgtType):
        if wgtType == 1:
                for (i,j) in G.E:
                  G.setWgt((i,j), G.deg(i)*G.deg(j))
        if wgtType == 4:
                for (i,j) in G.E:
                  G.setWgt((i,j), 1./G.deg(i)*G.deg(j))
        return G

def main():
        m = 2           # numbers of neighbors added per time-step
        nSamp = 100     # number of samples to average over
        wgtType = 1     # type of weight distribution

        # prepare files for simulated data
        #baseName = "wgtType%d_m%d_nSamp%d.pmf"%(wgtType,m,nSamp)
        #outFile = open("efficiency_"+baseName,'a')
        outFile=sys.stdout

        for N in [int(sqrt(2)**i) for i in range(12,26)]:
          aList = []
          for s in range(nSamp):
                # construct mst for scale free graphs
                # with given weight distribution
                G = scaleFreeGraph(N,m,s)
                G = setWgt(G,wgtType)
                T,Twgt = mstKruskal(G)

                # accumulate data
                Gwgt = sum(map(lambda e: G.wgt(e),G.E))
                aList.append(float(Twgt)/Gwgt)
          av,sDev,sErr = basicStatistics(aList)
          outFile.write("%d %lf %lf \n"%(N,av,sErr))

main()
