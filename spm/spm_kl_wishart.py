from spm._runtime import Runtime


def spm_kl_wishart(*args, **kwargs):
    r"""
      KL divergence between two Wishart densities  
        FORMAT [kl] = spm_kl_wishart(q,Q,p,P)  
         
        Calculate KL (Q||P) = <log Q/P> where avg is wrt Q  
        between two Wishart densities Q and P  
         
        q,Q      Parameters of first density  
        p,P      Parameters of first density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_kl_wishart.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_kl_wishart", *args, **kwargs)
