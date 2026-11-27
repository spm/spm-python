from spm._runtime import Runtime


def spm_mci_glike_deriv(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_glike_deriv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_glike_deriv", *args, **kwargs)
