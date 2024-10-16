from spm.__wrapper__ import Runtime


def spm_vb_lambda(*args, **kwargs):
  """  Variational Bayes for GLM-AR models - Update lambda  
    FORMAT [block] = spm_vb_lambda(Y,block)  
     
    Y      - [T x N] time series   
    block  - data structure (see spm_vb_glmar)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_vb_lambda.m)
  """

  return Runtime.call("spm_vb_lambda", *args, **kwargs)
