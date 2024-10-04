from spm.__wrap__ import _Runtime


def spm_contrasts(*args, **kwargs):
  """  Compute and store contrast parameters and inference SPM{.}  
    FORMAT SPM = spm_contrasts(SPM,Ic)  
     
    SPM  - SPM data structure  
    Ic   - indices of xCon to compute  
     
    This function fills in SPM.xCon and writes con_????, ess_???? and  
    spm?_???? images.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_contrasts.m)
  """

  return _Runtime.call("spm_contrasts", *args, **kwargs)
