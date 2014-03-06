## \file   scipy_MLE_sigma.py
#  \brief  maximum likelihood estimation of sigma
#          
#  \author OM
#  \date   17.04.2012
import sys
import scipy
import scipy.stats
import scipy.optimize
from MCS2012_lib import fetchData, bootstrap

def myMleEstimate(myFunc,par,data):

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

        objFunc = lambda s: -lnL_av(data,s)

        # maximize av log-likelihood
        par_mle = scipy.optimize.fmin(objFunc,par,disp=0)

        return par_mle

fileName  = sys.argv[1]
nBoot = int(sys.argv[2]) 

rawData  = fetchData(fileName,1,float)

# model function
Rayleigh = lambda s,x: scipy.stats.rayleigh.pdf(x,scale=s)

# simplified objective function: callable as objFunc(data)
# where data refers to a list of observations
objFunc = lambda x: myMleEstimate(Rayleigh,7.1,x)

s_av,s_Err = bootstrap(rawData,objFunc,nBoot)
print "# sigma = %lf +/- %lf (MLE)"%(s_av,s_Err)
