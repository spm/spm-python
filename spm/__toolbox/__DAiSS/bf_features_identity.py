from spm.__wrapper__ import Runtime


def bf_features_identity(*args, **kwargs):
  """  Identity matrix for cases when covariance is not necessary  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_identity.m)
  """

  return Runtime.call("bf_features_identity", *args, **kwargs)
