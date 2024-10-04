from spm.__wrap__ import _Runtime


def _checkfreq(*args, **kwargs):
  """  last input is always the required string  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/checkfreq.m)
  """

  return _Runtime.call("checkfreq", *args, **kwargs)
