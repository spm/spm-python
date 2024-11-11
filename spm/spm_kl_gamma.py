from spm.__wrapper__ import Runtime


def spm_kl_gamma(*args, **kwargs):
    """
      KL divergence between two Gamma densities  
        FORMAT [d] = spm_kl_gamma(b_q,c_q,b_p,c_p)  
         
        KL (Q||P) = <log Q/P> where avg is wrt Q  
         
        b_q, c_q    Parameters of first Gamma density  
        b_p, c_p    Parameters of second Gamma density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_kl_gamma.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_kl_gamma", *args, **kwargs)
