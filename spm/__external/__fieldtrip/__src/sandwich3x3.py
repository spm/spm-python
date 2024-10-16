from spm.__wrapper__ import Runtime


def sandwich3x3(*args, **kwargs):
  """  SANDWICH3X3 compute x*y*x' provided y is Hermitian and dimensionality is 3x3xN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/sandwich3x3.m)
  """

  return Runtime.call("sandwich3x3", *args, **kwargs)
