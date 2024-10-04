from spm.__wrap__ import _Runtime


def ft_keyval2cfg(*args, **kwargs):
  """  FT_KEYVAL2CFG converts between a structure and a cell-array with key-value  
    pairs which can be used for optional input arguments.   
      
    Use as  
      [cfg] = ft_keyval2cfg(varargin)  
     
    See also FT_CFG2KEYVAL, FT_GETOPT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_keyval2cfg.m)
  """

  return _Runtime.call("ft_keyval2cfg", *args, **kwargs)
