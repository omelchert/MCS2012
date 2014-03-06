import sys
from MCS2012_lib import *

## parse command line arguments
fileName     = sys.argv[1]
col          = int(sys.argv[2])

## construct approximate pmf from data
rawData      = fetchData(fileName,col)
av,sDev,sErr = basicStatistics(rawData)

print "av   = %4.3lf"%av
print "sErr = %4.3lf"%sErr
print "sDev = %4.3lf"%sDev
