from spm._runtime import Runtime


def spm_mci_check(*args, **kwargs):
    r"""
      Check model structure M is correctly specified  
        FORMAT [corr] = spm_mci_check (M)  
         
        corr      1 for correctly specified model  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/mci/inference/spm_mci_check.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_check", *args, **kwargs)
