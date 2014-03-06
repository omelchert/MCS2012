## \file   myHist_oop.py
#  \brief  object oriented implementation of 
#          a histogram data structure
#
#  due to the implemenation using the @property
#  decorator, this below code needs at least 
#  python version 2.2 to run propertly, see
#
#  http://docs.python.org/library/functions.html#property
# 
#  for more information and workarrounds
# 
#  (supplementary material MCS2012) 
#
#  \author OM
#  \date   XX.02.2011
from math import sqrt,floor

class simpleStats(object):
	def __init__(self):
		self._N    =0	
		self._av   =0.   
		self._Q    =0.   
		
	def add(self,val):
		self._N+=1
		dum = val-self._av
		self._av+= float(dum)/self._N
		self._Q+=dum*(val-self._av)
	
        @property
	def av(self): return self._av
	
        @property
	def sDev(self): return sqrt(self._Q/(self._N-1))
		
        @property
	def sErr(self): return self.sDev/sqrt(self._N)
	
	
class myHist(object):

	def __init__(self,xMin,xMax,nBins):
		self._min   = min(xMin,xMax)
		self._max   = max(xMin,xMax)
		self._cts   = 0
		self._nBins = nBins
		
		self._bin   = [0]*(nBins+2)
		self._norm  = None
		self._dx    = float(self._max-self._min)/self._nBins

		self._stats = simpleStats()
	
	def __binId(self,val):   
		return int(floor((val-self._min)/self._dx))

	def __bdry(self,bin):	  
		return self._min+bin*self._dx, self._min+(bin+1)*self._dx

	def __GErr(self,bin): 
		q=self._norm[bin]*self._dx
		return sqrt(q*(1-q)/(self._cts-1))/self._dx 

	def __normalize(self):
		self._norm = map(lambda x: float(x)/(self._cts*self._dx)  ,self._bin)

        @property
	def av(self): return self._stats.av
	
        @property
	def sDev(self): return self._stats.sDev
	
        @property
	def sErr(self): return self._stats.sErr

	def addValue(self, val):
		self._stats.add(val)
		if val<self._min:
			self._bin[self._nBins]+=1
		elif val>=self._max:
			self._bin[self._nBins+1]+=1
		else:
			self._bin[self.__binId(val)]+=1
		self._cts+=1

	def __str__(self):
		"""represent histogram as string"""
		self.__normalize()
		myStr ='# min  = %lf\n'%(float(self._min))
		myStr+='# max  = %lf\n'%(float(self._max))
		myStr+='# dx   = %lf\n'%(float(self._dx))
		myStr+='# av   = %lf (sErr = %lf)\n'%(self.av,self.sErr)
		myStr+='# sDev = %lf\n'%(self.sDev)
		myStr+='# xLow xHigh p(xLow <= x < xHigh) Gaussian_error\n'
		for bin in range(self._nBins): 
			low,up=self.__bdry(bin)
			myStr+='%lf %lf %lf %lf\n'%(low,up,self._norm[bin], self.__GErr(bin))
		return myStr
# EOF: myHist_oop.py
