from spm.__wrap__ import _Runtime


def _checkpos(*args, **kwargs):
  """  last input is always the required string  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/checkpos.m)
  """

  return _Runtime.call("checkpos", *args, **kwargs)
