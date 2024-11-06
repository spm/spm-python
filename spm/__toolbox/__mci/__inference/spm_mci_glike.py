from spm.__wrapper__ import Runtime


def spm_mci_glike(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_glike.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_glike", *args, **kwargs)
