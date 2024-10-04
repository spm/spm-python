from spm.__wrap__ import _Runtime


def _ismatch(*args, **kwargs):
  """  ISMATCH returns true if x is a member of array y, regardless of the class  
    of x and y, if y is a string, or a cell-array of strings, it can contain  
    the wildcard '*'  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/trialfun/private/ismatch.m)
  """

  return _Runtime.call("ismatch", *args, **kwargs)
