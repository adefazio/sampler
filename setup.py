from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

import Cython.Compiler.Options
# Output the html page for each file
Cython.Compiler.Options.annotate = True

setup(
    cmdclass = {'build_ext': build_ext},
    include_dirs = [numpy.get_include()],
    ext_modules=[
        Extension("fast_sampler", ["fast_sampler.pyx"], #"random_fast.cpp"
            language="c++",         
            libraries=["stdc++"],
            include_dirs=[numpy.get_include()]),
    ],
)
