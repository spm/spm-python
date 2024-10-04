from spm.__wrap__ import _Runtime


def mtimes2x2(*args, **kwargs):
  """  MTIMES2X2 compute x*y where the dimensionatity is 2x2xN or 2x2xNxM  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/mtimes2x2.m)
  """

  return _Runtime.call("mtimes2x2", *args, **kwargs)
