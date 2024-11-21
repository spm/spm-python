from spm.__wrapper__ import Runtime


def spm_vb_get_R(*args, **kwargs):
    """
      Get posterior correlation matrix for regression coefficients  
        FORMAT [R] = spm_vb_get_R(slice,h0)  
          
        slice  - data structure (see spm_vb_glmar)  
          
        R      - posterior correlation matrix of regression coefficients  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_vb_get_R.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_vb_get_R", *args, **kwargs)
