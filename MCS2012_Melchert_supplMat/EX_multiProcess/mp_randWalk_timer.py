from __future__ import division
from timeit import Timer

nSamp=10
def main_time():
    for N in [2**i for i in range(24)]:
       t1 = Timer("randWalk_multiproc(%d,%d)"%(N,nSamp),
                  "from mp_benchmark import randWalk_multiproc"
                  ).timeit(number=1)
       t2 = Timer("randWalk_seq(%d,%d)"%(N,nSamp),
                  "from mp_benchmark import randWalk_seq"
                  ).timeit(number=1)
       print N,t1/nSamp,t2/nSamp,t2/t1

main_time()
