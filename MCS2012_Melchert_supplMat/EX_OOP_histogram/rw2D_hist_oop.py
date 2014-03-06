import sys
from myHist_oop import myHist
from MCS2012_lib import fetchData

def main():
        ## parse command line args
        fName = sys.argv[1]
        col   = int(sys.argv[2])
        nBins = int(sys.argv[3])

        ## get data from file
        myData = fetchData(fName,col,float)

        ## assemble histogram
        h = myHist(min(myData),max(myData),nBins)
        for val in myData:
                h.addValue(val)
        print h

main()
## EOF: rw2D_hist_oop.py
