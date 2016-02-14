
# Weighted sampling with replacement, with dynamic weights

This code solves the problem of weighted sampling from a set, when you want to change the weight of a sample after you sample it. The implementation is described in the blog post [here](http://www.aarondefazio.com/tangentially/?p=58). The technique used is not novel, indeed it is based on publications from the 1960s.

A Cython implementation is provided along with the regular Python implementation.

Requires numpy and py.test packages.