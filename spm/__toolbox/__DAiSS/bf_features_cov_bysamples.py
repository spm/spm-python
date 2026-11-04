from spm._runtime import Runtime


def bf_features_cov_bysamples(*args, **kwargs):
    r"""
      Simple covariance computation to handle variable width WOIs,   
        Requires S.samples as a [1 x samples x ntrials] matrix of logical indices  
        indicating which data points should be used in the cov estimation  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_features_cov_bysamples.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_features_cov_bysamples", *args, **kwargs)
