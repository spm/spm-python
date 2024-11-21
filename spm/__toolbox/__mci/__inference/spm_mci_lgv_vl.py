from spm.__wrapper__ import Runtime


def spm_mci_lgv_vl(*args, **kwargs):
    """
      Sampling using Langevin Monte Carlo on path from VL solution  
        FORMAT [M,stats] = spm_mci_lgv_vl (mcmc,M,U,Y,vl,beta)  
         
        mcmc  Sampling parameters  
              .verbose            display progress  
              .maxits             maximum number of total samples   
              .init               initial sample values (start of chain)  
              .h                  step size  
         
        M     Model Structure  
              .dL                 Gradients and curvatures are computed using   
                                  this user-specified function. If this is absent  
                                  they will be computed using (i) the forward  
                                  sensitivity method for dynamical models   
                                  (ie. if M.f exists) or (ii) finite differences  
                                  otherwise  
                                    
        U     Inputs  
        Y     Data  
        vl    Variational Laplace solution  
              .Ep                 Posterior Mean  
              .Cp                 Posterior Covariance  
        beta  Inverse Temperature (0 at VL solution, 1 at posterior)  
         
        M     Updated model structure  
        stats Structure with fields:  
         
        .P     Samples, [maxits x M.Np]   
        .E     Negative log joint prob, [maxits x 1]  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_lgv_vl.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_lgv_vl", *args, **kwargs)
