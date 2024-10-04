from spm.__wrap__ import _Runtime


def spm_vb_a(*args, **kwargs):
  """  Update AR coefficients in VB GLM-AR model   
    FORMAT [block] = spm_vb_a(Y,block)  
     
    Y      - [T x N] time series   
    block  - data structure (see spm_vb_glmar)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_a.m)
  """

  return _Runtime.call("spm_vb_a", *args, **kwargs)
