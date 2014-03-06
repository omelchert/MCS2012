## \file   scipy_fitSigma.py
#  \brief  illustrate fit to a parametric 
#          function using the scipy module
#	   
#  scipy.optimize.leastsq does not yield error 
#  estimates for fit-parameters. As a remedy,
#  one might use bootstrap resampling to get an
#  impression of the respective errors
#
#  supplementary material MCS2012   
#
#  \author OM
#  \date   19.03.2012
import sys
import scipy
import scipy.optimize as sciOpt 
import scipy.stats as sciStat 
from MCS2012_lib import fetchData, bootstrap

def myFit(data,nBins=30):

        # data binning
        freqObs,xMin,dx,nOut = sciStat.histogram(data,nBins)

        # prepare observed x,y-Values
        N = len(data)
        xVals = [xMin + (i+0.5)*dx for i in range(nBins)]
        yVals = [freqObs[i]/(N*dx) for i in range(nBins)]
        
        # define objective function as the vertical difference
        # between the observed data and the fit-function
        fitFunc = lambda s,x: sciStat.rayleigh.pdf(x,scale=s)
        objFunc = lambda s,x,y: (y - fitFunc(s,x))

        # set initial guess for the fit-parameter and perform
        # least squares fit
        s0=7.
        s,flag = sciOpt.leastsq(objFunc,s0,args=(xVals,yVals))

        print s[0]
        return s[0]

def sigma(rawData):
        return scipy.sqrt(sum(map(lambda x:x*x,rawData))*0.5/len(rawData))

fileName  = sys.argv[1]
nBootSamp = int(sys.argv[2]) 

rawData  = fetchData(fileName,1,float)
#s1,s1_Err  = bootstrap(rawData,sigma,nBootSamp)
s2,s2_Err  = bootstrap(rawData,myFit,nBootSamp)

#print "# sigma = %lf +/- %lf"%(s1,s1_Err)
print "# sigma = %lf +/- %lf (least-squares fit)"%(s2,s2_Err)
# EOF: scipy_fitSigma.py
