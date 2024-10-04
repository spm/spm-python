from spm.__wrap__ import _Runtime


def spm_vb_w(*args, **kwargs):
  """  Variational Bayes for GLM-AR modelling in a block - update w  
    FORMAT [block] = spm_vb_w (Y,block)  
     
    Y          - [T x N] time series   
    block      - data structure (see spm_vb_glmar)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_w.m)
  """

  return _Runtime.call("spm_vb_w", *args, **kwargs)
