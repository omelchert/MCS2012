## \file   hist.py
#  \brief  minimal example to illustrate how to
#	   create a histogram with linear data 
#	   binning
#	   
#  supplementary material MCS2012 
#
#  \author OM
#  \date   04.03.2011
import sys
from MCS2012_lib import fetchData, hist_linBinning

## parse command line args
fName = sys.argv[1]
col   = int(sys.argv[2])
nBins = int(sys.argv[3])

## get data from file
myData = fetchData(fName,col,float)

## data binning procedure
hist_linBinning(myData,min(myData),max(myData),nBins) 

## EOF: hist.py
