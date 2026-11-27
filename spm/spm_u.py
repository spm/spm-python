from spm._runtime import Runtime


def spm_u(*args, **kwargs):
    r"""
      Uncorrected critical height threshold at a specified significance level  
        FORMAT [u] = spm_u(a,df,STAT)  
        a     - critical probability - {alpha}  
        df    - [df{interest} df{error}]  
        STAT  - Statistical field  
                      'Z' - Gaussian field  
                      'T' - T - field  
                      'X' - Chi squared field  
                      'F' - F - field  
                      'P' - P - value  
         
        u     - critical height {uncorrected}  
       __________________________________________________________________________  
         
        spm_u returns the uncorrected critical threshold at a specified   
        significance.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_u.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_u", *args, **kwargs)
