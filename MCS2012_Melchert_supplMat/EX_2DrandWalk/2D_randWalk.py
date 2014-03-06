## \file   2D_randWalk.py
#  \brief  simulate 2d random walk 
# 
#  supplementary material MCS2012  
#
#  \author OM
#  \date   XX.02.2011
from random import seed, random
from math import sqrt, cos,sin,pi

N=100000
n=1000
for s in range(n):	
   seed(s)
   x=y=0.
   for i in range(N):
      phi = random()*2*pi
      x   += cos(phi)
      y   += sin(phi)
   print s,sqrt(x*x+y*y)

## EOF: 2D_randWalk.py 
