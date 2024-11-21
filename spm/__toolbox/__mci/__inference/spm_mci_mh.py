from spm.__wrapper__ import Runtime


def spm_mci_mh(*args, **kwargs):
    """
      Metropolis Hastings with Gaussian priors and proposals  
        FORMAT [P,L,D] = spm_mci_mh (mcmc,M,U,Y)  
          
        mcmc      Optimisation parameters  eg.  
         
        .nsamp    number of samples to return   
        .Cprop    proposal density  
        .init     initial parameter point  
         
        M         Model structure  
        U         Inputs  
        Y         Data   
         
        P         Posterior samples   
        L         Logjoint history  
        D         Diagnostics (D.accept_rate, D.els)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_mh.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_mh", *args, **kwargs)
