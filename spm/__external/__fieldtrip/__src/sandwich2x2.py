from spm.__wrap__ import _Runtime


def sandwich2x2(*args, **kwargs):
  """  SANDWICH2X2 compute x*y*x' provided y is Hermitian and dimensionality is 2x2xN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/sandwich2x2.m)
  """

  return _Runtime.call("sandwich2x2", *args, **kwargs)
