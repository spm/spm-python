from spm.__wrap__ import _Runtime


def _keyval(*args, **kwargs):
  """  KEYVAL returns the value that corresponds to the requested key in a  
    key-value pair list of variable input arguments  
     
    Use as  
      [val] = keyval(key, varargin)  
     
    See also VARARGIN  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/keyval.m)
  """

  return _Runtime.call("keyval", *args, **kwargs)
