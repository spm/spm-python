from spm.__wrapper__ import Runtime


def _ismatch(*args, **kwargs):
  """  ISMATCH returns true if x is a member of array y, regardless of the class  
    of x and y, if y is a string, or a cell-array of strings, it can contain  
    the wildcard '*'  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/ismatch.m)
  """

  return Runtime.call("ismatch", *args, **kwargs)
