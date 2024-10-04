from spm.__wrap__ import _Runtime


def _standardise(*args, **kwargs):
  """  STANDARDISE computes the zscore of a matrix along dimension dim  
    has similar functionality as the stats-toolbox's zscore function  
     
    Use as  
      x = standardise(x, dim)  
     
    See also ZSCORE  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/standardise.m)
  """

  return _Runtime.call("standardise", *args, **kwargs)
