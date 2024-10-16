from spm.__wrapper__ import Runtime


def mtimes3x3(*args, **kwargs):
  """  MTIMES3X3 compute x*y where the dimensionatity is 3x3xN or 3x3xNxM  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/mtimes3x3.m)
  """

  return Runtime.call("mtimes3x3", *args, **kwargs)
