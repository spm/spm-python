from spm.__wrapper__ import Runtime


def bf_features_vbfa(*args, **kwargs):
  """  Variational Bayes Factor Analysis for computing noise covariance  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_vbfa.m)
  """

  return Runtime.call("bf_features_vbfa", *args, **kwargs)
