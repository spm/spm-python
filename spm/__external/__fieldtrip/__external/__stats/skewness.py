from spm._runtime import Runtime


def skewness(*args, **kwargs):
    r"""
      S = SKEWNESS(X, FLAG, DIM) computes the skewness of the values in X along the   
        dimention DIM. FLAG determines whether the bias is corrected. (0: bias  
        is corrected, 1: bias is not corrected (default)).  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/external/stats/skewness.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("skewness", *args, **kwargs)
