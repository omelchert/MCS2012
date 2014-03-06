import sys,math
from MCS2012_lib import fetchData 

rawData      = fetchData(sys.argv[1],1,float)

sum2=0.
for val in rawData: sum2+=val*val
print "sigma=",math.sqrt(sum2/(2.*len(rawData)))
