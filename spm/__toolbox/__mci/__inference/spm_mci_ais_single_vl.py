from spm._runtime import Runtime


def spm_mci_ais_single_vl(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_ais_single_vl.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_ais_single_vl", *args, **kwargs)
