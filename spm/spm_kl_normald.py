from spm.__wrapper__ import Runtime


def spm_kl_normald(*args, **kwargs):
    """
      KL divergence between two Gaussians with, possibly, diagonal covariances  
        FORMAT [d] = spm_kl_normald(m_q,c_q,m_p,c_p)  
         
        Calculate the KL distance KL (Q||P) = <log Q/P> where avg is wrt Q  
        between two Normal densities Q and P  
         
        m_q, c_q    Mean and covariance of first Normal density  
        m_p, c_p    Mean and covariance of second Normal density  
          
        If c_q and c_p are diagonal, pass them as vectors, and KL will  
        be computed more efficiently. Both must be full or both must be diagonal.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_kl_normald.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_kl_normald", *args, **kwargs)
