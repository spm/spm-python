from spm.__wrap__ import _Runtime


def bf_regularise_roi(*args, **kwargs):
  """  ROI regularisation  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_regularise_roi.m)
  """

  return _Runtime.call("bf_regularise_roi", *args, **kwargs)
