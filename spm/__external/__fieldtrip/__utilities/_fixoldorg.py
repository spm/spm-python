from spm.__wrap__ import _Runtime


def _fixoldorg(*args, **kwargs):
  """  FIXOLDORG use "old/new" instead of "org/new"  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixoldorg.m)
  """

  return _Runtime.call("fixoldorg", *args, **kwargs)
