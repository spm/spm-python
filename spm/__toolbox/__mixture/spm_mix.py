from spm.__wrapper__ import Runtime


def spm_mix(*args, **kwargs):
    """
      Fit a multivariate Gaussian Mixture model using VB  
        FORMAT [mix] = spm_mix (y,m,verbose)  
         
        y          [N x d] data matrix containing N samples of d-dim data  
        m          Number of mixture components  
        verbose    Set to 1 to see evolution of free energy, 0 otherwise  
                   (default=1)  
         
        mix        Returned model  
         
       --------------------------------------------------------------------------  
        The fields in mix are:  
         
        m                The number of components  
        fm               The negative free energy. This decomposes into  
                         fm=acc-kl_proportions-kl_covs-kl_centres  
         
        acc              model accuracy  
        kl_proportions   complexity penalty for cluster proportions  
        kl_covs          complexity penalty for cluster covariances  
        kl_centres       complexity penalty for cluster centres  
         
        Fields:  
         
        lambda           Post mixers, q(pi|D) = D(lambda)  
        gamma            [m x N] matrix of belonging probabilities  
        state(s).a       Post precisions, q(Gamma|D)=W(a,B)  
        state(s).B     
        state(s).C       Post covariance  
        state(s).m       Post mean, q(mu|D)=N(m_s,beta_s Gamma_s)  
        state(s).beta  
        state(s).prior   Estimated mixing proportions  
         
                         In the field prior:  
         
        lambda_0         Prior mixers, p(pi) = D(lambda_0)  
        a_0,B_0          Prior precisions, p(Gamma)=W(a_0,B_0)  
        m_0,beta_0       Prior means, p(mu)=N(m_0,beta_0 Gamma_s)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mixture/spm_mix.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mix", *args, **kwargs)
