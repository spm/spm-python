from spm.__wrapper__ import Runtime


def spm_Volt_W(*args, **kwargs):
    """
      Return basis functions used for Volterra expansion  
        FORMAT [W] = spm_Volt_W(u)  
        u  - times {seconds}  
        W  - basis functions (mixture of Gammas)  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_Volt_W.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_Volt_W", *args, **kwargs)
