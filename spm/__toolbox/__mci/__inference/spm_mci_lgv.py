from spm.__wrapper__ import Runtime


def spm_mci_lgv(*args, **kwargs):
    """
      Sampling using Langevin Monte Carlo  
        FORMAT [M,stats] = spm_mci_lgv (mcmc,M,U,Y)  
         
        mcmc  Sampling parameters  
              .verbose            display progress  
              .maxits             maximum number of total samples   
              .init               initial sample values (start of chain)  
              .update_obs_noise   estimate observation noise  
              .update_obs_step    update obs noise after this number of samples  
              .restart            restart chain from init   
              .h                  step size  
              .adapt_h            adapt h based on acceptance rate  
         
        M     Model Structure  
              .dL                 Gradients and curvatures are computed using   
                                  this user-specified function. If this is absent  
                                  they will be computed using (i) the forward  
                                  sensitivity method for dynamical models   
                                  (ie. if M.f exists) or (ii) finite differences  
                                  otherwise  
                                    
        U     Inputs  
        Y     Data  
         
        M     Updated model structure  
        stats Structure with fields:  
         
        .P     Samples, [maxits x M.Np]   
        .E     Negative log joint prob, [maxits x 1]  
         
        Uses Simplified Manifold Metropolis Adjusted Langevin   
        Algorithm (Simplified MMALA).   
         
        The manifold matrix captures local curvature but local changes   
        in it are ignored [1,2]. The manifold matrix is more simply   
        interpreted as the posterior covariance under local linear   
        assumptions.  
          
        [1] Calderhead and Girolami. Interface Focus (2011), pp 821-835.  
        [2] Girolami and Calderhead. J R Stat Soc B (2011), pp 123-214.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_lgv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_lgv", *args, **kwargs)
