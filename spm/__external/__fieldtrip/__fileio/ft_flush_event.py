from spm._runtime import Runtime


def ft_flush_event(*args, **kwargs):
    r"""
      FT_FLUSH_EVENT removes all events from the event queue  
         
        Use as  
          ft_flush_event(filename, ...)  
         
        See also FT_FLUSH_HEADER, FT_FLUSH_DATA  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_flush_event.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_flush_event", *args, **kwargs, nargout=0)
