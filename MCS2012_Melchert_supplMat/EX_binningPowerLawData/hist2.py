## \file   hist2.py
#  \brief  minimal example to illustrate how to
#	   create a histogram with logarithmic data 
#	   binning
#	   
#  supplementary material MCS2012 
#
#  \author OM
#  \date   04.03.2011
import sys
from MCS2012_lib import fetchData, hist

## parse command line arguments
fName = sys.argv[1]
nBins = int(sys.argv[2])

## get data from file
myData = fetchData(fName,0,float)

## logarithmic data binning procedure
hist(myData,[min(myData),max(myData)],nBins,'log')

## EOF: hist2.py
