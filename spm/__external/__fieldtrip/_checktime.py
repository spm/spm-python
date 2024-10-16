from spm.__wrapper__ import Runtime


def _checktime(*args, **kwargs):
  """  last input is always the required string  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/checktime.m)
  """

  return Runtime.call("checktime", *args, **kwargs)
