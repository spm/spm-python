from spm._runtime import Runtime


def spm_Volt_W(*args, **kwargs):
    r"""
      Return basis functions used for Volterra expansion  
        FORMAT [W] = spm_Volt_W(u)  
        u  - times {seconds}  
        W  - basis functions (mixture of Gammas)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_Volt_W.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_Volt_W", *args, **kwargs)
