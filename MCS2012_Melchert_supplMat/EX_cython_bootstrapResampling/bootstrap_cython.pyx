## \file   bootstrap_cython.py
#  \brief  bootstrap routine, optimized for 
#          speed using cython
#	   
#  supplementary material MCS2012 
#
#  \author OM
#  \date   14.03.2012
from MCS2012_lib import basicStatistics

# provide access to generic c-functions
cdef extern from "stdlib.h":
        double myCrand "drand48"()
        void myCsrand "srand48"(unsigned int seed)

# declare datatypes where possible
def bootstrap(list array,estimFunc,int nBootSamp=128):
        # datatypes fo for-loop indices are most 
        # important since cython does very well
	# at improving iteration speed of for-loops
        cdef int sample, val
        cdef int nMax = len(array)		
        cdef list h = [0.0]*nBootSamp
        cdef list bootSamp = [0.0]*nMax 
        origEstim=estimFunc(array)
	# the for ... from ... statement yields
	# a further improvement of running time 
	# using cython
        for sample from 0<=sample<nBootSamp:
          for val from 0<=val<nMax:
            bootSamp[val]=array[int(nMax*myCrand())]
          h[sample]=estimFunc(bootSamp)
        resError = basicStatistics(h)[1]
        return origEstim,resError

# EOF: bootstrap_cython.py
