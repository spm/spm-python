from spm._runtime import Runtime


def spm_uc_Bonf(*args, **kwargs):
    r"""
      Corrected critical height threshold at a specified significance level  
        FORMAT [u] = spm_uc_Bonf(a,df,STAT,S,n)  
        a     - critical probability - {alpha}  
        df    - [df{interest} df{residuals}]  
        STAT  - Statistical field  
                'Z' - Gaussian field  
                'T' - T - field  
                'X' - Chi squared field  
                'F' - F - field  
                'P' - P - value  
        S     - Voxel count  
        n     - number of conjoint SPMs  
         
        u     - critical height {corrected}  
       __________________________________________________________________________  
         
        spm_uc_Bonf returns the corrected critical height threshold at a  
        specified significance level (a). If n > 1, a conjunction probability  
        over the n values of the statistic is returned.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/spm_uc_Bonf.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_uc_Bonf", *args, **kwargs)
