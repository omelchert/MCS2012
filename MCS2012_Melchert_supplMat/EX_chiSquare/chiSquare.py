## \file   chiSquare.py
#  \brief  minimal example to illustrate 
#	   chi-square test
# 
#  supplementary material MCS2012 
#
#  \author OM
#  \date   XX.03.2011
import sys
from math import factorial as fac
from MCS2012_lib import *

## if the python module scipy is installed on your
## system, you might compute the corresponding
## p-value by means of the incomplete gamma function
## implemented in scipy.special
#remove comment# import scipy.special

## parse command line arguments
fileName     = sys.argv[1]
col          = int(sys.argv[2])
R            = int(sys.argv[3])

## construct approximate pmf from data
rawData      = fetchData(fileName,col)
pmf 	     = getPmf(rawData)

## func defs for symmetric binomial distrib
def bin(n,k): return fac(n)/(fac(n-k)*fac(k))
def f(x,N):   return bin(N,(x+N)*0.5)*0.5**N

## obtain observed/expected frequencies
## lump togheter small frequency bins, i.e.
## those for x>=R and x<=-R, to form super 
## bins that contain more events
N=len(rawData)
R=40
oFr={}
eFr={}
for el in pmf:
	if el >= R:  
		if R not in oFr:
			oFr[R] = eFr[R] = 0
		oFr[R]+=pmf[el]*N
		eFr[R]+=f(el,100)*N
	elif el <= -R:  
		if -R not in oFr:
			oFr[-R] = eFr[-R] = 0
		oFr[-R]+=pmf[el]*N
		eFr[-R]+=f(el,100)*N
	else: 
		oFr[el]=pmf[el]*N
		eFr[el]=f(el,100)*N

## get list of observed/expected freqs.
o = map(lambda x: x[1], oFr.items())
e = map(lambda x: x[1], eFr.items())

## perform chi-square test
dof,chi2=chiSquare(o,e,1)
print "# dof=%d, chi2=%5.3lf"%(dof,chi2)
print "# reduced chi2=%5.3lf"%(chi2/dof)

#remove comment# Qvalue = scipy.special.gammaincc(dof*0.5,chi2*0.5)
#remove comment# print "# p= %5.3lf"%(Qvalue)
## EOF: chiSquare.py
