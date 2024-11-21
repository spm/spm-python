from spm.__wrapper__ import Runtime


def spm_P_Bonf(*args, **kwargs):
    """
      Return the corrected P value using Bonferroni  
        FORMAT P = spm_P_Bonf(Z,df,STAT,S,n)  
         
        Z     - height {minimum over n values}  
        df    - [df{interest} df{error}]  
        STAT  - Statistical field  
              'Z' - Gaussian field  
              'T' - T - field  
              'X' - Chi squared field  
              'F' - F - field  
        S     - Voxel count  
        n     - number of conjoint SPMs  
         
        P     - corrected   P value  - P(STAT > Z)  
         
       __________________________________________________________________________  
         
        spm_P_Bonf returns the p-value of Z corrected by the Bonferroni  
        inequality.   
         
        If n > 1 a conjunction probability over the n values of the statistic  
        is returned.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/spm_P_Bonf.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_P_Bonf", *args, **kwargs)
