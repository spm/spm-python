from spm.__wrapper__ import Runtime


def spm_cov2corr(*args, **kwargs):
  """  Correlation matrix given the covariance matrix  
    FORMAT R = spm_cov2corr(C)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cov2corr.m)
  """

  return Runtime.call("spm_cov2corr", *args, **kwargs)
