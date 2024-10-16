from spm.__wrapper__ import Runtime


def _calctangent(*args, **kwargs):
  """  Based on calcrads.m, only difference is that RDip is alread  
    with respect to the sphere origin in calctangent.m  
    MODIFIED 13th JAN 2005 MATT BROOKES  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/calctangent.m)
  """

  return Runtime.call("calctangent", *args, **kwargs)
