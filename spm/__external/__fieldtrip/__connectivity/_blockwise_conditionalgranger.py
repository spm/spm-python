from spm.__wrapper__ import Runtime


def _blockwise_conditionalgranger(*args, **kwargs):
  """  BLOCKWISE_CONDITIONALGRANGER  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/blockwise_conditionalgranger.m)
  """

  return Runtime.call("blockwise_conditionalgranger", *args, **kwargs)
