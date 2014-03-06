## \file   droPyt.py
#  \brief  useful functions for the purpose of plotting
#          DendROgrams using PYThon
#
#  \author OM
#  \date 19.03.2012
from svgFigure_oop import *
from copy import *

def _getNodeOrder(tree):
        nodeOrder = []
        _nodeOrder_helper(tree,nodeOrder)
        return nodeOrder

def _nodeOrder_helper(nodes,nodeOrder):
        if type(nodes)==list:
             for n in nodes:
                _nodeOrder_helper(n,nodeOrder)
        else: 
                nodeOrder.append(nodes)

def _compute_leaveNodeOrder_xPos(bottomUpView,N):
        topDownView = dict((m,[]) for m in range(2*N-1))
        tree = dict((m,[]) for m in range(2*N-1))

        for node,succ in sorted(bottomUpView.iteritems()):
                topDownView[succ].append(node)
                if node >= N:
                   node = tree[node]
                tree[succ].append(node)

        # recursively determine leave order
        nodeOrder = _getNodeOrder(tree[2*N-2])

        # compute xPos of all nodes
        xPos = {}
        for i in range(2*N-1):
                if i <N:
                  xPos[nodeOrder[i]]=i*1./N
                else:
                  xPos[i]=0.5*(xPos[topDownView[i][0]]+xPos[topDownView[i][1]])

        return nodeOrder,xPos

def _tree2svg(myFigure,bottomUpView,xPos,yPos):
        M=len(xPos)
        scaleW = myFigure._w
        scaleH = myFigure._h
        for i in range(M-1):
                j  = bottomUpView[i]
                xi,yi = scaleW*xPos[i],scaleH*yPos[i]
                xj,yj = scaleW*xPos[j],scaleH*yPos[j]

	        myFigure.line(xi,-yi,xi,-yj,scaleW*0.01)
	        myFigure.line(xi,-yj,xj,-yj,scaleW*0.01)
        return myFigure

def _tree2svg_horizontal(myFigure,bottomUpView,xPos,yPos):
        M=len(xPos)
        scaleW = myFigure._w
        scaleH = myFigure._h
        for i in range(M-1):
                j  = bottomUpView[i]
                xi,yi = scaleW*xPos[i],-scaleH*yPos[i]
                xj,yj = scaleW*xPos[j],-scaleH*yPos[j]

	        myFigure.line(yi,xi,yj,xi,scaleW*0.0025)
	        myFigure.line(yj,xi,yj,xj,scaleW*0.0025)

        return myFigure

def _distMat2svg(myFigure,Dij,leaveNodeOrder,N):
        d = myFigure._w/N
        for i in range(N):
          for j in range(N):
                colVal = 100.*Dij[leaveNodeOrder[i]][leaveNodeOrder[j]]
                color  = "rgb(%lf,%lf,%lf)"%(colVal,colVal,colVal)
	        myFigure.rectangle(i*d,(j+0.5)*d,d,d,d*0.01,col=color ,fillCol=color)
        return myFigure

def _colorBar2svg(myFigure,nSteps=14):
        colBar_w=myFigure._w/20
        x=myFigure._w*1.05
        dx=colBar_w
        dy=0.9*myFigure._w/nSteps

        yOff = 0.1*myFigure._w
        textSize=7.
        myFigure.text(x,(nSteps+0.5)*dy+yOff,textSize,'dissimilartiy:',dx=0.5*textSize,dy=0.,rot=-90)

        x+=textSize*0.7
        for i in range(nSteps):
                y =(i+0.5)*dy + yOff
                colVal= (nSteps-i)*256./nSteps
                color  = "rgb(%lf,%lf,%lf)"%(colVal,colVal,colVal)
	        myFigure.rectangle(x,y,dx,dy,dx*0.05,col='rgb(0,0,0)' ,fillCol=color)

        myFigure.text(x+dx,0.5*dy +yOff,textSize,'1.0',dx=0.,dy=textSize*0.5)
        myFigure.text(x+dx,(0.5*nSteps+0.5)*dy+yOff,textSize,'0.5',dx=0.,dy=0)
        myFigure.text(x+dx,(nSteps+0.5)*dy+yOff,textSize,'0.0',dx=0.,dy=-textSize*0.5)
        return myFigure

def _heightBar2svg(myFigure):
        x  = myFigure._w*1.05	
        dx = myFigure._w/20
        dy = myFigure._h

        textSize=7.
        
        myFigure.text(x,0.,textSize,'height:',dx=0.,dy=0.,rot=-90)

        x+=textSize*0.7


        myFigure.line(x,0,x,-dy,myFigure._w*0.01)

        myFigure.line(x,0,x+dx/2,0.,myFigure._w*0.01)
        myFigure.line(x,-0.5*dy,x+dx/2,-0.5*dy,myFigure._w*0.01)
        myFigure.line(x,-dy,x+dx/2,-dy,myFigure._w*0.01)

        myFigure.text(x+dx,0.,textSize,'0.0',dx=0.,dy=textSize*0.5)
        myFigure.text(x+dx,-0.5*dy,textSize,'0.5',dx=0.,dy=textSize*0.5)
        myFigure.text(x+dx,-dy,textSize,'1.0',dx=0.,dy=textSize*0.5)

        return myFigure

def _leaveNames2svg_horizontal(myFigure,nameList,nodeOrder,xPos,yPos):
        N=len(nameList)
        scaleW = myFigure._w
        scaleH = myFigure._h
        x=0.
        textSize=2.
        for i in range(N):
                j  = nodeOrder[i]
                yj = scaleW*xPos[j]
                myFigure.text(x,yj,textSize,nameList[j],dx=textSize,dy=textSize*0.25)

        return myFigure

def droPyt_fetchBottomUpView_sciPy(clusterResult,N):
        m=N
        yPos = [0.]*(N+N-1)
        bottomUp = {}
        for i,j,h,n in clusterResult:

                # m is predecessor of iNew and jNew
                bottomUp[int(i)]=m
                bottomUp[int(j)]=m

                # height of node m is simply h
                yPos[m] = h

                m+=1

        # ensure that maximal yPos = 1.
        yPos/=max(yPos)
        return bottomUp,yPos

def droPyt_rawData_sciPy(Dij,clusterResult,N):
        bottomUpView,yPos = droPyt_fetchBottomUpView_sciPy(clusterResult,N)
        print 'p ',N
        for i in range(N):
          for j in range(N):
             if i>j:
                print 'd ', i,j, Dij[i][j]

        for i,j in sorted(bottomUpView.iteritems()):
                print 'c ', i,j, yPos[i]

def droPyt_rawData_fromFile(fName):
        N=None
        dataFile =  open(fName,"r")
        for line in dataFile:
                token = line.split()
                if len(token)>1 and line[0]!='#':
                        if token[0]=='p':
                                N=int(token[1])
                                Dij = [[0.]*N for i in range(N) ]
                                bottomUpView = {}
                                yPos  = [1.]*(2*N-1)
                        elif token[0]!='p' and N==None:
                                print "ERROR: need problem line first"
                        else:
                                if token[0]=='d':
                                        i   = int(token[1])
                                        j   = int(token[2])
                                        dij = float(token[3])
                                        Dij[i][j]=dij
                                        Dij[j][i]=dij
                                elif token[0]=='c':
                                        i   = int(token[1])
                                        j   = int(token[2])
                                        hi = float(token[3])
                                        bottomUpView[i]=j
                                        yPos[i]=hi
        return N,Dij,bottomUpView,yPos

def droPyt_distMat_dendrogram_sciPy(Dij,clusterResult,N):
        bottomUpView,yPos = droPyt_fetchBottomUpView_sciPy(clusterResult,N)
        droPyt_distMat_dendrogram(Dij,bottomUpView,yPos,N)

def droPyt_dendrogram_leaveNames_sciPy(nameList,clusterResult,N):
        bottomUpView,yPos = droPyt_fetchBottomUpView_sciPy(clusterResult,N)
        droPyt_dendrogram_leaveNames(nameList,bottomUpView,yPos,N)

def droPyt_dendrogram(bottomUpView,yPos,N):
        leaveNodeOrder,xPos = _compute_leaveNodeOrder_xPos(bottomUpView,N)
	myFigure = mySVG(width=100.,heigth=100./3.)
        myFigure = _tree2svg(myFigure,bottomUpView,xPos,yPos)
        myFigure.saveFile()

def droPyt_distMat_dendrogram(Dij,bottomUpView,yPos,N,putHeightBar=1,putColorBar=1):
        leaveNodeOrder,xPos = _compute_leaveNodeOrder_xPos(bottomUpView,N)
	myFigure = mySVG(width=100.,heigth=100./3.)
        myFigure = _tree2svg(myFigure,bottomUpView,xPos,yPos)
        myFigure = _distMat2svg(myFigure,Dij,leaveNodeOrder,N)
        if putColorBar:
                myFigure = _colorBar2svg(myFigure)
        if putHeightBar:
                myFigure = _heightBar2svg(myFigure)

        myFigure.saveFile()


def droPyt_dendrogram_leaveNames(nameList,bottomUpView,yPos,N,putHeightBar=1,putColorBar=1):
        leaveNodeOrder,xPos = _compute_leaveNodeOrder_xPos(bottomUpView,N)
	myFigure = mySVG(width=200.,heigth=200./6.)
        myFigure = _tree2svg_horizontal(myFigure,bottomUpView,xPos,yPos)
        myFigure = _leaveNames2svg_horizontal(myFigure,nameList,leaveNodeOrder,xPos,yPos)
        myFigure.saveFile()


if __name__=='__main__':

        import sys

        N,Dij,bottomUpView,yPos=droPyt_rawData_fromFile(sys.argv[1])
        droPyt_distMat_dendrogram(Dij,bottomUpView,yPos,N)

