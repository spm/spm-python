from spm.__wrapper__ import Runtime


def spm_kl_eig_normal(*args, **kwargs):
    """
      KL divergence between normal densities using eigendecomposition   
        function [d] = spm_kl_eig_normal (m_q,c_q,c_p)  
         
        Calculate the KL distance   
         
        KL (Q||P) = <log Q/P> where avg is wrt Q  
         
        between two Normal densities Q and P where P is  
        zero mean and has a diagonal covariance.  
         
        m_q, c_q    Mean and covariance of first Normal density  
        c_p         Covariance of second (zero-mean) Normal density  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/spectral/spm_kl_eig_normal.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_kl_eig_normal", *args, **kwargs)
