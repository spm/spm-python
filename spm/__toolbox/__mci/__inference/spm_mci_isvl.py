from spm.__wrapper__ import Runtime


def spm_mci_isvl(*args, **kwargs):
    """
      Compute Log Evidence using Importance Sampling   
        FORMAT [isvl] = spm_mci_isvl (mcmc,M,U,Y,VL)  
         
        mcmc          Optimisation parameters  eg.  
         
        .maxits       number of samples to use  
         
        M             Model structure   
        U             Input structure  
        Y             Data   
         
        isvl            
        .logev         log evidence  
        .L(s)          log likelihood of sth sample  
        .v(s)          importance weight of sth sample  
        .logev_est(S)  estimate based on first S samples only  
        .logev_boot(b) estimate based on bth bootstrap resample (of size .maxits)  
         
        Uses IS with VL posterior as proposal  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_isvl.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_isvl", *args, **kwargs)
