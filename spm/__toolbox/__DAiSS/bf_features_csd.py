from spm.__wrapper__ import Runtime


def bf_features_csd(*args, **kwargs):
  """  Compute cross-spectral density matrix for DICS  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_csd.m)
  """

  return Runtime.call("bf_features_csd", *args, **kwargs)
