from spm._runtime import Runtime


def spm_kl_gamma(*args, **kwargs):
    r"""
      KL divergence between two Gamma densities  
        FORMAT [d] = spm_kl_gamma(b_q,c_q,b_p,c_p)  
         
        KL (Q||P) = <log Q/P> where avg is wrt Q  
         
        b_q, c_q    Parameters of first Gamma density  
        b_p, c_p    Parameters of second Gamma density  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_kl_gamma.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_kl_gamma", *args, **kwargs)
