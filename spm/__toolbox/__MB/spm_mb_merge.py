from spm.__wrap__ import _Runtime


def spm_mb_merge(*args, **kwargs):
  """  Combine tissue maps together  
    FORMAT out = spm_mb_merge(cfg)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_merge.m)
  """

  return _Runtime.call("spm_mb_merge", *args, **kwargs)
