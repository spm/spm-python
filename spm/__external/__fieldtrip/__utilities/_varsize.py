from spm.__wrap__ import _Runtime


def _varsize(*args, **kwargs):
  """  VARSIZE returns the size of a variable in bytes. It can be used on any MATLAB  
    variable, including structures and cell arrays.  
     
    See also WHOS  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/varsize.m)
  """

  return _Runtime.call("varsize", *args, **kwargs)
