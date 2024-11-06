from spm.__wrapper__ import Runtime


def spm_uc_RF(*args, **kwargs):
    """
      Corrected critical height threshold at a specified significance level  
        FORMAT [u] = spm_uc_RF(a,df,STAT,R,n)  
        a     - critical probability - {alpha}  
        df    - [df{interest} df{residuals}]  
        STAT  - Statistical field  
                'Z' - Gaussian field  
                'T' - T field  
                'X' - Chi-squared field  
                'F' - F field  
        R     - RESEL Count {defining search volume}  
        n     - number of conjoint SPMs  
         
        u     - critical height {corrected}  
         
       __________________________________________________________________________  
         
        spm_uc returns the corrected critical threshold at a specified significance  
        level (a). If n > 1 a conjunction probability over the n values of the  
        statistic is returned.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_uc_RF.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_uc_RF", *args, **kwargs)
