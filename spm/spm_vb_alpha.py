from spm.__wrap__ import _Runtime


def spm_vb_alpha(*args, **kwargs):
  """  Variational Bayes for GLM-AR models - Update alpha   
    FORMAT [block] = spm_vb_alpha(Y,block)  
     
    Y      - [T x N] time series   
    block  - data structure (see spm_vb_glmar)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_alpha.m)
  """

  return _Runtime.call("spm_vb_alpha", *args, **kwargs)
