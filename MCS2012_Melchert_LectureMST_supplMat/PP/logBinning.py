import sys
from math import floor,sqrt,exp,log


def fetchPmf(fName):
	"""collect data from a specified column of a
	supplied file

	Input:
	fName	-- path to file
	col	-- no of the column (default is 0)
	dataType-- expected data type (default is int)

	Returns: (myList)
	myList	-- resulting list of numbers
	"""
	myList=[]
	file = open(fName,"r")
	for line in file: 
	   stuff = line.split()
	   if len(stuff)>=1 and stuff[0]!='#':
		## cast the value stored in column col
		## to type dataType and append to list 
		myList += [int(stuff[0])]*int(stuff[1])
	file.close()
	return myList

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


def main():
        myList = fetchPmf(sys.argv[1])
        hist(myList,(min(myList),max(myList)),nBins=21,mode='log')



main()        
