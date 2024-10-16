from spm.__wrapper__ import Runtime


def _fixoldorg(*args, **kwargs):
  """  FIXOLDORG use "old/new" instead of "org/new"  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixoldorg.m)
  """

  return Runtime.call("fixoldorg", *args, **kwargs)
