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

def updateDegHist(T,dH):
        Vmst = dict()
        for i,j in T:
                Vmst[i] = Vmst.setdefault(i,0) + 1
                Vmst[j] = Vmst.setdefault(j,0) + 1
        for deg in Vmst.values():
                dH[deg] = dH.setdefault(deg,0)+1
        return dH

def updateWgtHist(T,G,dW):
        for e in T:
                wgt = G.wgt(e)
                dW[wgt] = dW.setdefault(wgt,0)+1
        return dW

def printHist(outFile,dH):
        norm = sum(dH.values())
        for key,cts in sorted(dH.iteritems()):
                outFile.write("%lf %d %lf\n"%( key,cts, cts*1./norm))

def main():
        N = 10000       # number of nodes in graph
        m = 2           # numbers of neighbors added per time-step
        nSamp = 100     # number of samples to average over
        wgtType = 4     # type of weight distribution

        # prepare files for simulated data
        baseName = "wgtType%d_N%d_m%d_nSamp%d.pmf"%(wgtType,N,m,nSamp)
        outFileDeg = open("deg_"+baseName,'w')
        outFileWgt = open("wgt_"+baseName,'w')

        # declare data structures for observables
        dH = dict()     
        dW = dict()        

        for s in range(nSamp):
                # construct mst for scale free graphs
                # with given weight distribution
                G = scaleFreeGraph(N,m,s)
                G = setWgt(G,wgtType)
                T,Twgt = mstKruskal(G)

                # accumulated data
                dH = updateDegHist(T,dH)
                dW = updateWgtHist(T,G,dW)

        # finally, store data in files
        printHist(outFileDeg,dH)
        printHist(outFileWgt,dW)
        

main()
