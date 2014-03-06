## \file   MCS2012_lib.py
#  \brief  tiny libary that contains useful functions
# 	   for data postprocesssing
#	   
#  supplementary material MCS2012 
#
#  \author OM
#  \date   04.03.2011
from math   import sqrt,floor,log,exp
from random import randint

def fetchData(fName,col=0,dataType=float):
	"""collect data from a specified column of a
	supplied file

	Input:
	fName	-- path to file
	col	-- no of the column (default is 0)
	dataType-- expected data type (default is int)

	Returns: (myList)
	myList	-- resulting list of numbers
	"""
	myList=[]  ## ini empty list		
	file = open(fName,"r")
	for line in file: 
	   stuff = line.split()
	   if len(stuff)>=1 and stuff[0]!='#':
		## cast the value stored in column col
		## to type dataType and append to list 
		myList.append(dataType(stuff[col]))
	file.close()
	return myList

def getPmf(myList):
	"""construct approximate pmf from values in 
	supplied list

	Input:
	myList	-- outcomes of random experiments for
		   which pmf shall be approximated

	Returns: (pMap)
	pMap	-- pmf of the values stored in myList
	"""
	pMap = {}  ## ini empty dictionary
	nInv=1./len(myList) 
	for element in myList:
	   pMap.setdefault(element,0.)
	   pMap[element] += nInv
	return pMap

def basicStatistics(myList):
	"""compute mean value, standard deviation,
	and standard error of the mean for the 
	supplied list of numerical values

	NOTE: so as to reduce roundoff errors, 
	variance is computed via the corrected
	two-pass algorithm

	Input:
	myList	-- sequence of numerical values

	Returns: (av,sDev,sErr)
	av	-- mean value
	sDev	-- standard deviation
	sErr	-- standard error of the mean
	"""
	av=var=tiny=0.
	N=len(myList) 
	for el in myList: 
		av += el
	av /= N
	for el in myList:
		dum   = el - av
		tiny += dum
		var  += dum*dum
	var = (var - tiny*tiny/N)/(N-1)
	sDev = sqrt(var)
	sErr = sDev/sqrt(N)
	return av, sDev, sErr

def bootstrap(array,estimFunc,nBootSamp=128):
	"""Empirical bootstrap resampling of data.
	
	estimates value of function 'estimFunc' from original data 
	stored in list 'array'. Calculates corresponding error as 
	standard deviation of the 'nBootSamp' resampled bootstrap 
	data sets

	Input:
	array     	-- list of values for resampling procedure
	estimFunc  	-- estimator function for resampling procedure
	nBootSamp  	-- number of bootstrap samples (default 128)

	Returns: (origEstim,resError)
	origEstim	-- value of estimFunc for original data
	resError	-- corresponding error estimated via resampling
	"""
	# estimate mean value from original array
	origEstim=estimFunc(array)
	## resample data from original array
	nMax=len(array)		
	h   = [0.0]*nBootSamp
	bootSamp = [0.0]*nMax 
	for sample in range(nBootSamp):
		for val in range(nMax):
			bootSamp[val]=array[randint(0,nMax-1)]
		h[sample]=estimFunc(bootSamp)
	## estimate error as std deviation of resampled values
	resError = basicStatistics(h)[1]
	return origEstim,resError



def hist_linBinning(rawData,xMin,xMax,nBins=10):
	"""histogram using linear binning of supplied data

	Input:
	rawData	-- list containing data to be binned 
	xMin    -- lower boundary for numerical values (inclusive)
	xMax    -- upper boundary for numerical values (exclusive)
	nBin    -- desired number of bins (default =10)

	Returns: (nothing)
	"""
	h = [0]*nBins		## initial frequencies for each bin
	dx = (xMax-xMin)/nBins	## uniform bin width

	## get bin id that corresponds to supplied numerical value
	def binId(val):   return int(floor((val-xMin)/dx))
	## get lower and upper boundary for supplied bin id
	def bdry(bin):	  return xMin+bin*dx, xMin+(bin+1)*dx
	## compute gaussian error bar for particular bin
	def GErr(q,n,dx): return sqrt(q*(1-q)/(N-1))/dx 

	## data binning procedure: obtain frequencies
	for value in rawData:
		if 0<=binId(value)<nBins:
		  h[binId(value)] += 1
	
	## dump histogram
	N=sum(h) ## overall number of events
	for bin in range(nBins):
		hRel   = float(h[bin])/N ## normalized freq.
		low,up = bdry(bin)
		width  = up-low
		print low, up, hRel/width, GErr(hRel,N,width) 

def hist(rawData,xRange,nBins=10,mode='lin'):
	"""histogram using linear binning of supplied data

	Input:
	rawData	-- list containing data to be binned 
	xRange  -- lower(incl)/upper(excl) boundary for numerical values
	nBin    -- desired number of bins (default =10)
	mode	-- binning type (possible choices: lin, log)

	Returns: (nothing)
	"""

	h = [0]*nBins
	xMin=float(xRange[0])
	xMax=float(xRange[1])

	if mode == 'lin':
		dx = (xMax-xMin)/nBins
		def binId(val):   return int(floor((val-xMin)/dx))
		def bdry(bin):	  return xMin+bin*dx, xMin+(bin+1)*dx
		def GErr(q,n,dx): return sqrt(q*(1-q)/(N-1))/dx 

	elif mode == 'log':
		dx = log(xMax/xMin)/nBins
		def binId(val):   return int(floor(log(val/xMin)/dx))
		def bdry(bin):	  return xMin*exp(bin*dx), xMin*exp((bin+1)*dx)
		def GErr(q,n,dx): return "##" 

	for value in rawData:
		if 0<=binId(value)<nBins:
		  h[binId(value)] += 1
	
	N=sum(h)
	for bin in range(nBins):
		hRel   = float(h[bin])/N
		low,up = bdry(bin)
		width  = up-low
		print low, up, hRel/width, GErr(hRel,N,width) 


def chiSquare(obsFreq,expFreq,nConstr):
	"""perform chi-square test for supplied
	list of data

	Input:
	obsFreq	-- observed frequencies
	expFreq -- expected frequencies

	Returns: (dof,chi2)
	dof	-- number of degrees of freedom
	chi2	-- numerical value of chi-square
	"""
	nBins=len(obsFreq)
	chi2=0.0
	for bin in range(nBins):
		dum   = obsFreq[bin]-expFreq[bin]
		chi2 += dum*dum/expFreq[bin]
	dof = nBins-nConstr
	return dof,chi2


## EOF: MCS2012_lib.py
