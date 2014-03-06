import sys
from MCS2012_lib import *

## parse command line arguments
fileName     = sys.argv[1]
col          = int(sys.argv[2])

## construct approximate pmf from data
rawData      = fetchData(fileName,col)
pmf 	     = getPmf(rawData)

## dump pmf/distrib func. to standard outstream
FX=0.
for endpos in sorted(pmf):
	FX+=pmf[endpos]
	print endpos,pmf[endpos],FX

