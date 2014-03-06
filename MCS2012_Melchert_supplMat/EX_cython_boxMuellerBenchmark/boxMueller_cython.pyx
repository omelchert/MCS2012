
cdef extern from "math.h":
        double sin(double)
        double log(double)
        double sqrt(double)
        double M_PI

cdef extern from "stdlib.h":
         double drand48()
         void srand48(unsigned int)

cdef double gaussRand(double mu,double sigma):
        cdef double u1,u2,r,phi
        u1 = drand48()
        u2 = drand48()
        r   = sqrt(-2.*log(u1))
        phi = 2.*M_PI*u2
        return mu+sigma*r*sin(phi)

def main_cython(N,mu,sigma):
        cdef int i
        srand48(0)
        for i from 0<=i<N:
                z = gaussRand(mu,sigma)

