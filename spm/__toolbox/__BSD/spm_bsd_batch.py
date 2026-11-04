from spm._runtime import Runtime


def spm_bsd_batch(*args, **kwargs):
    r"""
      SPM Configuration file for Bayesian Spectral Decomposition (BSD)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/spm_bsd_batch.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_bsd_batch", *args, **kwargs)
