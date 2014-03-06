## \file   rw2d_analysis_scipy.py
#  \brief  illustrate data analysis
#          using the scipy module
#	   
#  supplementary material MCS2012   
#
#  \author OM
#  \date   19.03.2012
import sys
import scipy, scipy.stats
from MCS2012_lib import fetchData 

def myPdf(x): return scipy.stats.rayleigh.pdf(x,scale=sigma)
def myCdf(x): return scipy.stats.rayleigh.cdf(x,scale=sigma)

fileName = sys.argv[1]
nBins  = int(sys.argv[2]) 

rawData  = fetchData(fileName,1,float)

# Basic statistics using scipy
print '## Basic statistics using scipy'
print '# data file:', fileName
N     = len(rawData)
sigma = scipy.sqrt(sum(map(lambda x:x*x,rawData))*0.5/N)
av    = scipy.mean(rawData)
sDev  = scipy.std(rawData)
print '# N     =', N
print '# av    =', av 
print '# sDev  =', sDev 
print '# sigma =', sigma

print '## Histogram using scipy'
limits = (min(rawData),max(rawData))
freqObs,xMin,dx,nOut =\
        scipy.stats.histogram(rawData,nBins,limits)
# reconstruct bin boundaries
bdry = [(xMin+i*dx ,xMin+(i+1)*dx) for i in range(nBins)]

print '# nBins = ', nBins
print '# xMin  = ', xMin 
print '# dx    = ', dx   
print '# (binCenter) (pdf-observed) (pdf-rayleigh distrib.)'
for i in range(nBins):
        x = 0.5*(bdry[i][0]+bdry[i][1]) 
        print x, freqObs[i]/(N*dx), myPdf(x) 

print '## Chi2 - test using scipy'
# compute expected frequencies
freqExp = scipy.array(
           [N*(myCdf(x[1])-myCdf(x[0])) for x in bdry])

chi2,p = scipy.stats.chisquare(freqObs,freqExp,ddof=1)
print '# chi2     = ', chi2
print '# chi2/dof = ', chi2/(nBins-1)
print '# pVal     = ', p

import scipy.optimize
import numpy

xVals = []
yVals = []
for i in range(nBins):
        xVals.append(0.5*(bdry[i][0]+bdry[i][1])) 
        yVals.append(freqObs[i]/(N*dx))

func    = lambda s,x: scipy.stats.rayleigh.pdf(x,scale=s)
errFunc = lambda s,x,y: (func(s,x)-y)

s = scipy.optimize.leastsq(errFunc,5.,args=(xVals,yVals),full_output=1)

print s
# EOF: rw2d_analysis_scipy.py
