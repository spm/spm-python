from spm.__wrap__ import _Runtime


def _checkchan(*args, **kwargs):
  """  last input is always the required string  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/checkchan.m)
  """

  return _Runtime.call("checkchan", *args, **kwargs)
