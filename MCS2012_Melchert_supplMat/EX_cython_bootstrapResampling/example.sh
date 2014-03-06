# build cython shared library
python setup.py build_ext --inplace

# time cython version of the bootstrap resampling code
time python main_bootstrap_cython.py  ../EX_1DrandWalk/N100_n100000.dat 24
