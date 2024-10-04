from spm.__wrap__ import _Runtime


def _blockwise_conditionalgranger(*args, **kwargs):
  """  BLOCKWISE_CONDITIONALGRANGER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/blockwise_conditionalgranger.m)
  """

  return _Runtime.call("blockwise_conditionalgranger", *args, **kwargs)
