from spm.__wrap__ import _Runtime


def bf_features_tdcov(*args, **kwargs):
  """  Simple band limited covariance computation with temporal decomposition  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_tdcov.m)
  """

  return _Runtime.call("bf_features_tdcov", *args, **kwargs)
