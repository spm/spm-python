from spm.__wrapper__ import Runtime


def ft_flush_event(*args, **kwargs):
    """
      FT_FLUSH_EVENT removes all events from the event queue  
         
        Use as  
          ft_flush_event(filename, ...)  
         
        See also FT_FLUSH_HEADER, FT_FLUSH_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_flush_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_flush_event", *args, **kwargs, nargout=0)
