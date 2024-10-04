from spm.__wrap__ import _Runtime


def _bf_fuse_lf(*args, **kwargs):
  """  Prepares lead-fields to match channels in covariance  
    Copyright (C) 2014 Wellcome Trust Centre for Neuroimaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/bf_fuse_lf.m)
  """

  return _Runtime.call("bf_fuse_lf", *args, **kwargs)
