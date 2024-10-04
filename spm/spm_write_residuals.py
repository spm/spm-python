from spm.__wrap__ import _Runtime


def spm_write_residuals(*args, **kwargs):
  """  Write residual images  
    FORMAT Vres = spm_write_residuals(SPM,Ic)  
    SPM    - structure containing generic analysis details  
    Ic     - contrast index used to adjust data (0:   no adjustment)  
                                                (NaN: adjust for everything)   
     
    VRes   - struct array of residual image handles  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_write_residuals.m)
  """

  return _Runtime.call("spm_write_residuals", *args, **kwargs)
