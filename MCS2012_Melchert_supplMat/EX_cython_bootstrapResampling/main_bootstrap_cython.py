## \file   bootstrap_minimal_cython.py
#  \brief  minimal example to illustrate unbiased
#	   error estimation via bootstrap resampling 
# 
#  supplementary material MCS2012  
#
#  \author OM
#  \date   XX.03.2011
import sys
from MCS2012_lib import fetchData,basicStatistics 
from bootstrap_cython import bootstrap

## parse command line arguments
fileName = sys.argv[1]
M        = int(sys.argv[2])

rawData  = fetchData(fileName,1)

def sDev(array): return basicStatistics(array)[1]

print "sDev: %5.3lf +/- %4.3lf"%bootstrap(rawData,sDev,M)
## EOF: bootstrap_minimal_cython.py
