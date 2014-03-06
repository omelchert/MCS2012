from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup(
	cmdclass = {'build_ext': build_ext},
	ext_modules = [Extension("boxMueller_cython", ["boxMueller_cython.pyx"])],  
)
# Usage: python setup.py build_ext --inplace
