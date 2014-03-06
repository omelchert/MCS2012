import multiprocessing 
import random
from math import sqrt,cos,sin,pi

class myProcess(multiprocessing.Process):
        def __init__(self,myRng,mySeed,Nsteps):
                self.myRng  = myRng
                self.mySeed = mySeed
                self.Nsteps = Nsteps
                multiprocessing.Process.__init__(self)

        def run(self):
                self.myRng.seed(self.mySeed)
                x=y=0.
                for i in range(self.Nsteps):
                   phi  = self.myRng.random()*2.*pi
                   x   += cos(phi)
                   y   += sin(phi)
 #               print self.mySeed,sqrt(x*x+y*y)

def randWalk_multiproc(N,nSamp):
        for s in range(nSamp):
                myRng   = random.Random()
                process = myProcess(myRng,s,N)
                process.start()

        while len(multiprocessing.active_children()):
                 pass

def randWalk_seq(N,nSamp):
        for s in range(nSamp):	
           random.seed(s)
           x=y=0.
           for i in range(N):
              phi = random.random()*2.*pi
              x   += cos(phi)
              y   += sin(phi)
#           print s,sqrt(x*x+y*y)
