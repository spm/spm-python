from spm.__wrap__ import _Runtime


def spm_mvb_bmc(*args, **kwargs):
  """  Multivariate Bayesian model comparison (Baysian decoding of a contrast)  
    FORMAT [F,P,MVB] = spm_mvb_bmc(mvb)  
     
    mvb   : models to compare (file names)  
    F     : F ratio relative to null  
    P     : P-value relative to null  
    MVB   : best model  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_mvb_bmc.m)
  """

  return _Runtime.call("spm_mvb_bmc", *args, **kwargs)
