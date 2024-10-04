from spm.__wrap__ import _Runtime


def spm_uc(*args, **kwargs):
  """  Corrected critical height threshold at a specified significance level  
    FORMAT [u] = spm_uc(a,df,STAT,R,n,S)  
    a     - critical probability - {alpha}  
    df    - [df{interest} df{residuals}]  
    STAT  - Statistical field  
            'Z' - Gaussian field  
            'T' - T - field  
            'X' - Chi squared field  
            'F' - F - field  
    R     - RESEL Count {defining search volume}  
    n     - number of conjoint SPMs  
    S     - Voxel count  
     
    u     - critical height {corrected}  
   __________________________________________________________________________  
     
    spm_uc returns the corrected critical height threshold at a specified  
    significance level (a), using the minimum of different valid methods.  
     
    See also: spm_uc_RF, spm_uc_Bonf  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_uc.m)
  """

  return _Runtime.call("spm_uc", *args, **kwargs)
