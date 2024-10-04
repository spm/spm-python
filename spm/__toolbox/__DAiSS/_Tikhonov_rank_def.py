from spm.__wrap__ import _Runtime


def _Tikhonov_rank_def(*args, **kwargs):
  """  Apply Tikhonov regularisation to rank-deficient matrix  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/Tikhonov_rank_def.m)
  """

  return _Runtime.call("Tikhonov_rank_def", *args, **kwargs)
