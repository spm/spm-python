from spm.__wrapper__ import Runtime


def spm_vb_gamma(*args, **kwargs):
  """  Variational Bayes for GLMAR model - Update gamma and get w_dev, wk_mean  
    FORMAT [block] = spm_vb_gamma(Y,block)  
     
    Y      - [T x N] time series  
    block  - data structure (see spm_vb_glmar)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_gamma.m)
  """

  return Runtime.call("spm_vb_gamma", *args, **kwargs)
