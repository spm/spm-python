from spm.__wrap__ import _Runtime


def bf_features_regmulticov(*args, **kwargs):
  """  Simple covariance computation with regularization  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_regmulticov.m)
  """

  return _Runtime.call("bf_features_regmulticov", *args, **kwargs)
