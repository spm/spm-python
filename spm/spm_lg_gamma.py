from spm._runtime import Runtime


def spm_lg_gamma(*args, **kwargs):
    r"""
      Log of generalised gamma function  
        FORMAT [lng] = spm_lg_gamma(p,b)  
         
        p       - dimension parameter  
        b       - degrees of freedom type parameter  
       __________________________________________________________________________  
         
        References:  
        * Bayesian Inference in Statistical Analysis, Box & Tiao, 1992, p. 427.  
        * Aspects of Multivariate Statistical Theory, R.J. Muirhead, p. 62.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_lg_gamma.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lg_gamma", *args, **kwargs)
