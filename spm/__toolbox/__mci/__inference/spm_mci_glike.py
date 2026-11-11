from spm._runtime import Runtime


def spm_mci_glike(*args, **kwargs):
    r"""
      Gaussian Log-likelihood   
        FORMAT [L,e,st] = spm_mci_glike (P,M,U,Y,G)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
        Y         Data  
        G         Predictions (computed if not provided)  
          
        L         Log Likelihood  
        e         Errors  
        st        Status flag (0 for OK, -1 for problem)  
         
        Assumes diagonal error covariance M.Ce  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_glike.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_glike", *args, **kwargs)
