from math import pi,sqrt,log,sin,cos
from random import seed,random

def gaussRand(mu,sigma):
        u1 = random()
        u2 = random()
        r   = sqrt(-2.*log(u1))
        phi = 2.*pi*u2
        return mu+sigma*r*sin(phi)

def main_python(N,mu,sigma):
        seed(0)
        for i in range(N):
                z1 = gaussRand(mu,sigma)

