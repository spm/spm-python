from spm.__wrap__ import _Runtime


def bf_features_csd(*args, **kwargs):
  """  Compute cross-spectral density matrix for DICS  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features_csd.m)
  """

  return _Runtime.call("bf_features_csd", *args, **kwargs)
