from spm.__wrap__ import _Runtime


def spm_cov2corr(*args, **kwargs):
  """  Correlation matrix given the covariance matrix  
    FORMAT R = spm_cov2corr(C)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/spm_cov2corr.m)
  """

  return _Runtime.call("spm_cov2corr", *args, **kwargs)
