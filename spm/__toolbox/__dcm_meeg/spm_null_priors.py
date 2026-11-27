from spm._runtime import Runtime


def spm_null_priors(*args, **kwargs):
    r"""
      Prior moments for null (Jacobian) model  
        FORMAT [pE,pC] = spm_null_priors(A,B,C)  
         
        A{1},B{m},C  - binary constraints on extrinsic connections  
         
        pE - prior expectation  
        pC - prior covariance  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/dcm_meeg/spm_null_priors.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_null_priors", *args, **kwargs)
