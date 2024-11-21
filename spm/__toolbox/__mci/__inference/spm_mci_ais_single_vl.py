from spm.__wrapper__ import Runtime


def spm_mci_ais_single_vl(*args, **kwargs):
    """
      Produce a single independent sample from posterior using AIS  
        FORMAT [P,E,logw,acc] = spm_mci_ais_single_vl (mcmc,M,U,Y,vl)  
         
        mcmc      Sampling settings  
        M         Model structure  
        U         Input structure  
        Y         Data  
        vl        Variational Laplace solution  
                      .Ep                 Posterior Mean  
                      .Cp                 Posterior Covariance  
         
        P         [Np x 1] sample  
        E         Negative log joint  
        logw      Contribution to model evidence  
        acc       acc(j) is acceptance rate at temperature j  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_ais_single_vl.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_ais_single_vl", *args, **kwargs)
