from spm.__wrapper__ import Runtime


def _mtimes2x2(*args, **kwargs):
  """  MTIMES2X2 compute x*y where the dimensionatity is 2x2xN or 2x2xNxM  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/mtimes2x2.m)
  """

  return Runtime.call("mtimes2x2", *args, **kwargs)
