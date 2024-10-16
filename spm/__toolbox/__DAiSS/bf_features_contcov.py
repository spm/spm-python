from spm.__wrapper__ import Runtime


def bf_features_contcov(*args, **kwargs):
  """  Robust covariance for continuous data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_contcov.m)
  """

  return Runtime.call("bf_features_contcov", *args, **kwargs)
