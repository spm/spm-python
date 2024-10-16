from spm.__wrapper__ import Runtime


def _ctranspose3x3(*args, **kwargs):
  """  compute ctranspose of multiple 3x3 matrices, input is 3x3xN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/ctranspose3x3.m)
  """

  return Runtime.call("ctranspose3x3", *args, **kwargs)
