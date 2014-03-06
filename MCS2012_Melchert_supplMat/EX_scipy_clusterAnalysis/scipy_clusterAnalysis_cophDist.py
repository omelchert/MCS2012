import sys
import scipy
import scipy.cluster.hierarchy as sch
import scipy.spatial.distance as ssd
from dumpDendrogram import droPyt_distMat_dendrogram_sciPy
from dumpDendrogram import droPyt_dendrogram_leaveNames_sciPy

def fetchDistMat(fileName):
        '''read distance matrix in DIMACS-format 
        from specified input file

        Input:
        fileName  - location of data file

        Returns: (nameList,Dij,N)
        nameList  - names of the variables that
                    comprise distance matrix
        Dij       - distance matrix in square form
        N         - number of variables
        '''
        N=None
        dataFile=open(fileName,"r")
        for line in dataFile:
          token = line.split()
          if len(token)>1 and line[0]!='#':
            if token[0]=='p':
                N=int(token[1])
                nameList = [0.]*N
                Dij  = scipy.zeros((N,N),dtype='d')
            elif token[0]!='p' and N==None:
                print "ERROR: need problem line first"
                sys.exit(1)
            else:
                if token[0]=='d':
                  i,j = int(token[1]),int(token[2])
                  Dij[i,j] = Dij[j,i] = float(token[3])
                elif token[0]=='n':
                  i = int(token[1])
                  nameList[i] = token[2]
        return nameList,Dij,N

def myDistMatrix_2D(N):
        '''2D distance matrix using euclidean distance

        Input:
        N   - number of variables

        Returns: (Dij)
        Dij - distance matrix in square form 
        '''
        scipy.random.seed(100)
        xVec = scipy.rand(N,2)
        Dij  = scipy.zeros((N,N),dtype='d')
        for i in range(N):
          for j in range(N):
            Dij[i,j] = ssd.euclidean(xVec[i],xVec[j]) 
        return Dij

def main():
        # fetch distance matrix from specified input file
        distMatFile = sys.argv[1]
        nameList,Dij_sq,N=fetchDistMat(distMatFile)

        # in scipy most routines operate on 'condensed'
        # distance matrices, i.e. upper triagonal matrices
        # the function square contained in the scipy.spatial
        # submodule might be used in order to switch from 
        # full square to condensed matrices and vice versa
        Dij_cd = ssd.squareform(Dij_sq)
        # hierarchical clustering where the distance between
        # two coordinates is the distance of the cluster
        # averages
        # cluster Result = 'top down view' of the hierarchical
        # clustering
        clusterResult = sch.linkage(Dij_cd, method='average')
        # returns cophenetic distances
        # corr = cophenetic correlation
        # Cij_cd = condensed cophenetic distance matrix
        corr,Cij_cd   = sch.cophenet(clusterResult,Dij_cd)
        Cij_sq = ssd.squareform(Cij_cd)

        # print dendrogram on top of cophenetic distance 
        # matrix to standard outstream
        droPyt_distMat_dendrogram_sciPy(Cij_sq,clusterResult,N)

main()
