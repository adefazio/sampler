
from numpy import *
from sampler import Sampler
from fast_sampler import FastSampler
from scipy.stats import binom

def test_simple():
    nentries = 5
    h = FastSampler(nentries, max_value=100, min_value=1)

    weights = array([1,1,3,5,2], dtype='d')
    normalized_weights = weights/sum(weights)

    for i in range(nentries):
        h.add(i, weights[i])
        
    nsamples = 100000
    distro = zeros(nentries)
    
    for i in range(nsamples):
        idx = h.sample()
        distro[idx] += 1
    
    normalized_distro = distro / sum(distro)
    
    print distro
    print weights
    print normalized_distro
    print normalized_weights

    # Statistical test on result
    cdf_vals = binom.cdf(k=distro, n=nsamples, p=normalized_weights)
    print "CDF VALS"
    print cdf_vals
    has_bad_vals = any(logical_or(cdf_vals <= 0.005, cdf_vals >= 0.995))
    # Will fail about 5% of the time due to statistics
    assert not has_bad_vals


def test_change():
    nentries = 5
    h = FastSampler(nentries, max_value=100, min_value=1)

    weights = array([1,1,3,5,2], dtype='d')
    normalized_weights = weights/sum(weights)

    for i in range(nentries):
        h.add(i, weights[i])
     
    new_weights = array([8,1.5,6,12,4], dtype='d')
    
    # change the weights
    for i in range(nentries):
        idx = h.sampleAndRemove()
        h.add(idx, new_weights[idx])
        weights[idx] = new_weights[idx]
      
    normalized_weights = weights/sum(weights)
        
    nsamples = 100000
    distro = zeros(nentries)
    
    for i in range(nsamples):
        idx = h.sample()
        distro[idx] += 1
    
    normalized_distro = distro / sum(distro)

    print "Distro"
    print distro
    print "Weights"
    print weights
    print "Normalized Distro"
    print normalized_distro
    print "Normalized Weights"
    print normalized_weights

    # Statistical test on result
    cdf_vals = binom.cdf(k=distro, n=nsamples, p=normalized_weights)
    print "CDF VALS"
    print cdf_vals
    has_bad_vals = any(logical_or(cdf_vals <= 0.005, cdf_vals >= 0.995))
    # Will fail about 5% of the time due to statistics
    assert not has_bad_vals
