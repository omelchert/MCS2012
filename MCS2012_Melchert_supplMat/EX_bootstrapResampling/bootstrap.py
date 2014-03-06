## \file   bootstrap.py
#  \brief  minimal example to illustrate unbiased
#	   error estimation via bootstrap resampling 
# 
#  supplementary material MCS2012 
#
#  \author OM
#  \date   XX.03.2011
import sys
from MCS2012_lib import *

## parse command line arguments
fileName = sys.argv[1]
M        = int(sys.argv[2])

## get data from file
rawData  = fetchData(fileName,1)

## define estimation functions
def mean(array): return basicStatistics(array)[0]
def sDev(array): return basicStatistics(array)[1]

## dump results of bootstrap resampling procedure
print "# estimFunc: q +/- dq"
print "mean: %5.3lf +/- %4.3lf"%bootstrap(rawData,mean,M)
print "sDev: %5.3lf +/- %4.3lf"%bootstrap(rawData,sDev,M)
## EOF: bootstrap.py
