from spm.__wrap__ import _Runtime


def _ft_error(*args, **kwargs):
  """  FT_ERROR prints an error message on screen, just like the standard ERROR function.  
     
    Use as  
      ft_error(...)  
    with arguments similar to fprintf, or  
      ft_error(msgId, ...)  
    with arguments similar to error.  
     
    See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/specest/private/ft_error.m)
  """

  return _Runtime.call("ft_error", *args, **kwargs)
