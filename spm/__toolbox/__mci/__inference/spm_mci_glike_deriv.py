from spm.__wrapper__ import Runtime


def spm_mci_glike_deriv(*args, **kwargs):
    """
      Gradient of Gaussian Log-likelihood   
        FORMAT [dLdp,iCpY,st,L] = spm_mci_glike_deriv (P,M,U,Y)  
         
        P         Parameters  
        M         Model structure  
        U         Inputs  
        Y         Data  
          
        dLdP      Gradient of Log Likelihood wrt params, [1 x Np]  
        iCpY      Curvature (Fisher Information)  
        st        status flag (0 for OK, -1 for problem)  
        L         Log Likelihood  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_glike_deriv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_glike_deriv", *args, **kwargs)
