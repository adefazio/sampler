from distutils.core import setup
from Cython.Build import cythonize
import numpy

import Cython.Compiler.Options
# Output the html page for each file
Cython.Compiler.Options.annotate = True

extra_args = ["-std=c++0x", "-stdlib=libc++"]

setup(
    ext_modules = cythonize(["*.pyx", "random_fast.cpp"],
        language="c++"),
    include_dirs = [numpy.get_include()],
)
