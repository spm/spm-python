from spm._runtime import Runtime


def spm_mci_check(*args, **kwargs):
    """
      Check model structure M is correctly specified  
        FORMAT [corr] = spm_mci_check (M)  
         
        corr      1 for correctly specified model  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/mci/inference/spm_mci_check.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_mci_check", *args, **kwargs)
