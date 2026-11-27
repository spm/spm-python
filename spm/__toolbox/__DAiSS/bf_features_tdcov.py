from spm._runtime import Runtime


def bf_features_tdcov(*args, **kwargs):
    r"""
      Simple band limited covariance computation with temporal decomposition  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_features_tdcov.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_features_tdcov", *args, **kwargs)
