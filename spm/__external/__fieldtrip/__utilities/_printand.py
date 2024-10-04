from spm.__wrap__ import _Runtime


def _printand(*args, **kwargs):
  """  PRINTAND prints a single or multiple strings as "x1, x2, x3 and x4". If there is  
    only one string, that string is returned without additional formatting.  
     
    See also PRINTOR  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/printand.m)
  """

  return _Runtime.call("printand", *args, **kwargs)
