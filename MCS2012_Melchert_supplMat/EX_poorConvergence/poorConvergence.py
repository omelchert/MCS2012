from random import seed, random
from MCS2012_lib import basicStatistics

## implement absolut deviation as robust
## estimator for given data
def absDev(av,seq):
	N = len(seq)
	aDev = 0.
	for val in seq:
		aDev += abs(val-av)
	return aDev/N

## inversion method to obtain power law
## distributed pseudo random numbers
N=100000
seed(0)
alpha=2.2
myList = []
for i in range(N):
	r=pow(1.-random() , -1./(alpha-1.)  )
	myList.append(r)

## basic statistics for different samplesizes to
## assess convergence properties for av and sDev
M=100; dN=N/M
for Nmax in [dN+i*dN for i in range(M)]:
	av,sDev,sErr=basicStatistics(myList[:Nmax])
	aDev = absDev(av,myList[:Nmax])
	print Nmax, av,sErr,sDev,aDev
