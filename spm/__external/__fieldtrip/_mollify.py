from spm.__wrap__ import _Runtime


def _mollify(*args, **kwargs):
  """  This function does something  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/mollify.m)
  """

  return _Runtime.call("mollify", *args, **kwargs)
