from spm._runtime import Runtime


def bf_regularise_clifftrunc(*args, **kwargs):
    r"""
      Regularisation based on the sudden drop-off in the covariance Eigenspectrum  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DAiSS/bf_regularise_clifftrunc.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_regularise_clifftrunc", *args, **kwargs)
