from spm.__wrap__ import _Runtime


def bf_features(*args, **kwargs):
  """  Prepare data features for filter computation  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_features.m)
  """

  return _Runtime.call("bf_features", *args, **kwargs)
