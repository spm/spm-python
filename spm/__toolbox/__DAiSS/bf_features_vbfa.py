from spm._runtime import Runtime


def bf_features_vbfa(*args, **kwargs):
    r"""
      Variational Bayes Factor Analysis for computing noise covariance  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_features_vbfa.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_features_vbfa", *args, **kwargs)
