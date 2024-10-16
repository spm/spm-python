from spm.__wrapper__ import Runtime


def ft_flush_event(*args, **kwargs):
  """  FT_FLUSH_EVENT removes all events from the event queue  
     
    Use as  
      ft_flush_event(filename, ...)  
     
    See also FT_FLUSH_HEADER, FT_FLUSH_DATA  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_flush_event.m)
  """

  return Runtime.call("ft_flush_event", *args, **kwargs, nargout=0)
