from spm.__wrapper__ import Runtime


def _standardise(*args, **kwargs):
  """  STANDARDISE computes the zscore of a matrix along dimension dim  
    has similar functionality as the stats-toolbox's zscore function  
     
    Use as  
      x = standardise(x, dim)  
     
    See also ZSCORE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/standardise.m)
  """

  return Runtime.call("standardise", *args, **kwargs)
