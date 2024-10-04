from spm.__wrap__ import _Runtime


def ft_info(*args, **kwargs):
  """  FT_INFO prints an info message on screen, depending on the verbosity   
    settings of the calling high-level FieldTrip function.  
     
    Use as  
      ft_info(...)  
    with arguments similar to fprintf, or  
      ft_info(msgId, ...)  
    with arguments similar to warning.  
     
    You can switch of all messages using  
      ft_info off  
    or for specific ones using  
      ft_info off msgId  
     
    To switch them back on, you would use   
      ft_info on  
    or for specific ones using  
      ft_info on msgId  
      
    Messages are only printed once per timeout period using  
      ft_info timeout 60  
      ft_info once  
    or for specific ones using  
      ft_info once msgId  
     
    You can see the most recent messages and identifier using  
      ft_info last  
     
    You can query the current on/off/once state for all messages using  
      ft_info query  
     
    See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_info.m)
  """

  return _Runtime.call("ft_info", *args, **kwargs)
