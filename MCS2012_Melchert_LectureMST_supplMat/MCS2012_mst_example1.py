import sys
from MCS2012_uGraphWeighted import uGraphWeighted
from MCS2012_mstKruskal import mstKruskal,mstGraphviz
import random

seed = random.seed
randInt = random.randint
pickNode = random.choice


def fetchGraph(fileName):
        '''read edge-list from specified file

        Input:
        fileName        - path to file containing edge-list

        Returns: (G)
        G               - directed graph 
        '''
	G=uGraphWeighted()
	file = open(fileName,"r")
	for line in file:
	    stuff = line.split()
            if len(stuff)>1 and line[0]!='#':
		G.addEdge(int(stuff[0]),int(stuff[1]),float(stuff[2]))
	file.close()
	return G

def main():

        G = fetchGraph(sys.argv[1])
        T,Twgt = mstKruskal(G) 

        print mstGraphviz(G,T)

main()
