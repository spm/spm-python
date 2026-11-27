from spm._runtime import Runtime


def bf_inverse_ebb(*args, **kwargs):
    r"""
      Computes Empirical Bayes Beamformer filters  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_inverse_ebb.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_inverse_ebb", *args, **kwargs)
