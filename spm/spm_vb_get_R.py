from spm.__wrap__ import _Runtime


def spm_vb_get_R(*args, **kwargs):
  """  Get posterior correlation matrix for regression coefficients  
    FORMAT [R] = spm_vb_get_R(slice,h0)  
      
    slice  - data structure (see spm_vb_glmar)  
      
    R      - posterior correlation matrix of regression coefficients  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_get_R.m)
  """

  return _Runtime.call("spm_vb_get_R", *args, **kwargs)
