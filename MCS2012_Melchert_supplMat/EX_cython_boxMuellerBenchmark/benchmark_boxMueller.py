## \file   benchmark_boxMueller.py
#  \brief  use python timeit module to benchmark
#          python and cython implementation of 
#          Box-Mueller method for the generation 
#          of Gaussian random deviates
#	   
#  supplementary material MCS2012 
#
#  \author OM
#  \date   14.03.2012
from timeit import Timer

N=10000000

# time PYTHON code
t_py = Timer("main_python(%d,0.,1.)"%(N),
             "from boxMueller_python import main_python"
             ).timeit(number=1)

# time CYTHON code
t_cy = Timer("main_cython(%d,0.,1.)"%(N),
             "from boxMueller_cython import main_cython"
             ).timeit(number=1)

print "# PYTHON vs CYTHON: Box-Mueller Benchmark test"
print "# number of random deviates N=",N 
print "# PYTHON: t_PY =",t_py
print "# CYTHON: t_CY =",t_cy
print "# speed-up factor t_PY/t_CY =",t_py/t_cy
# EOF: benchmark_boxMueller.py 
