from spm._runtime import Runtime


def spm_cov2corr(*args, **kwargs):
    r"""
      Correlation matrix given the covariance matrix  
        FORMAT R = spm_cov2corr(C)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_cov2corr.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cov2corr", *args, **kwargs)
