from spm.__wrap__ import _Runtime


def _ft_setopt(*args, **kwargs):
  """  FT_SETOPT assigns a value to an configuration structure or to a cell-array  
    with key-value pairs. It will overwrite the option if already present, or  
    append the option if not present.  
     
    Use as  
      s = ft_setopt(s, key, val)  
    where s is a structure or a cell-array.  
     
    See also FT_GETOPT, FT_CHECKOPT  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/inverse/private/ft_setopt.m)
  """

  return _Runtime.call("ft_setopt", *args, **kwargs)
