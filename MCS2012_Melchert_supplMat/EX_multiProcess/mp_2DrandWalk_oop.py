from math import sqrt,cos,sin,pi
import random
import multiprocessing 

class myProcess(multiprocessing.Process):
        def __init__(self,myLock,myRng,mySeed,Nsteps):
                self.myLock = myLock
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
                self.myLock.acquire()
                print self.mySeed,sqrt(x*x+y*y)
                self.myLock.release()

def main():
        N=10000
        nSamp = 5
        myLock  = multiprocessing.Lock()
        for s in range(nSamp):
                myRng   = random.Random()
                process = myProcess(myLock,myRng,s,N)
                process.start()

        for p in multiprocessing.active_children():
                print "random walk ID: ", p.mySeed


main()
