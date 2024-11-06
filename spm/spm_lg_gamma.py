from spm.__wrapper__ import Runtime


def spm_lg_gamma(*args, **kwargs):
    """
      Log of generalised gamma function  
        FORMAT [lng] = spm_lg_gamma(p,b)  
         
        p       - dimension parameter  
        b       - degrees of freedom type parameter  
       __________________________________________________________________________  
         
        References:  
        * Bayesian Inference in Statistical Analysis, Box & Tiao, 1992, p. 427.  
        * Aspects of Multivariate Statistical Theory, R.J. Muirhead, p. 62.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_lg_gamma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_lg_gamma", *args, **kwargs)
