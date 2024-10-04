from spm.__wrap__ import _Runtime


def _ctranspose2x2(*args, **kwargs):
  """  compute ctranspose of multiple 2x2 matrices, input is 2x2xN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/ctranspose2x2.m)
  """

  return _Runtime.call("ctranspose2x2", *args, **kwargs)
