## \file   scipy_fitSigma.py
#  \brief  illustrate fit to a parametric 
#          function using the scipy module
#	   
#  scipy.optimize.leastsq does not yield error 
#  estimates for fit-parameters. As a remedy,
#  one might use bootstrap resampling to get an
#  impression of the respective errors
#
#  \author OM
#  \date   19.03.2012
import sys
import scipy
import scipy.stats
import scipy.optimize
from MCS2012_lib import fetchData, bootstrap
from func_logLikelihood import lnL_ray_av

def myMleEstimate_fast(par,data):

        # use cython implementation of log-likelihood
        # using rayleigh function
        objFunc = lambda s: -lnL_ray_av(data,s)

        # maximize av log-likelihood
        par_mle = scipy.optimize.fmin(objFunc,par,disp=0)
        #par_mle = scipy.optimize.brent(objFunc,brack=(6.8,7.4))
        print par_mle[0] 
        return par_mle[0]

def myMleEstimate(myFunc,par,data):

        # actually, this one is a bit slow
        def lnL_av(x,par):
                N = len(x)
                # compute log-likelihood
                lnL = 0.
                for i in range(N):
                        lnL +=  scipy.log(myFunc(par,x[i]))

                # get average log-likelihood: estimate expected
                # log likelihood of a single observation
                print '#', lnL/N, par
                return lnL/N

        # use the cython implementation instead
        objFunc = lambda s: -lnL_ray_av(data,s)

        # maximize av log-likelihood
        par_mle = scipy.optimize.fmin(objFunc,par,disp=0)
        #par_mle = scipy.optimize.brent(objFunc,brack=(6.8,7.4))
        print '#',par_mle[0] 
        return par_mle[0]

def main():

        fileName  = sys.argv[1]
        nBoot = int(sys.argv[2]) 

        rawData  = fetchData(fileName,1,float)

        # model function
        #Rayleigh = lambda s,x: scipy.stats.rayleigh.pdf(x,scale=s)
        
        # simplified objective function: callable as objFunc(data)
        # where data refers to a list of observations
        # ... uses a fast cython implementation of the 
        # log-likelihood function using a rayleigh model function
        objFunc = lambda x: myMleEstimate_fast(7.1,x)

        av,sErr = bootstrap(rawData,objFunc,nBoot)
        print "# sigma = %lf +/- %lf (MLE)"%(av,sErr)


def main_1Dscan():

        fileName  = sys.argv[1]

        rawData  = fetchData(fileName,1,float)

        # model function
        Rayleigh = lambda s,x: scipy.stats.rayleigh.pdf(x,scale=s)

        def lnL_av(myFunc,x,par):
                N = len(x)
                # compute log-likelihood
                lnL = 0.
                for i in range(N):
                        lnL +=  scipy.log(myFunc(par,x[i]))

                # get average log-likelihood: estimate expected
                # log likelihood of a single observation
                return lnL/N
        
        objFunc = lambda s: lnL_ray_av(rawData,s)

        s=5.
        sMax=12.
        ds=0.05
        while (s<=sMax):
                f=objFunc(s)
                print s,f
                s+=ds




main()
#main_1Dscan()
