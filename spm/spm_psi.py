from spm._runtime import Runtime


def spm_psi(*args, **kwargs):
    r"""
      log normalised Dirichlet probability matrix (columns)  
        FORMAT [A] = spm_psi(a)  
         
        a  - Dirichlet parameter tensor  
         
        This routine returns the expectation of log marginals: E[log(X)]: X(i) ~  
        Beta(a(i),a0 - a(i)), for a > 1. See also: psi.m  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_psi.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_psi", *args, **kwargs)
