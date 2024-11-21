from spm.__wrapper__ import Runtime


def spm_mci_gprior_deriv(*args, **kwargs):
    """
      Gradient of Log Gaussian prior  
        FORMAT [j] = spm_mci_gprior_deriv (Pr,M)  
         
        Pr        parameters (vectorised and in M.V subspace)  
        M         model structure  
         
        j         gradient of log Gaussian prior  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_gprior_deriv.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_mci_gprior_deriv", *args, **kwargs)
