from spm._runtime import Runtime


def spm_mci_gprior_deriv(*args, **kwargs):
    r"""
      Gradient of Log Gaussian prior  
        FORMAT [j] = spm_mci_gprior_deriv (Pr,M)  
         
        Pr        parameters (vectorised and in M.V subspace)  
        M         model structure  
         
        j         gradient of log Gaussian prior  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_gprior_deriv.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_gprior_deriv", *args, **kwargs)
