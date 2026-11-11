from spm._runtime import Runtime


def ft_filter_event(*args, **kwargs):
    r"""
      FT_FILTER_EVENT does what its name implies  
         
        Use as  
          event = ft_filter_event(event, ...)  
         
        The optional arguments should come in key-value pairs and determine the  
        filter characteristics:  
          type         = cell-array with strings  
          value        = numeric array  
          sample       = numeric array  
          timestamp    = numeric array  
          offset       = numeric array  
          duration     = numeric array  
          minsample    = value  
          maxsample    = value  
          minduration  = value  
          maxduration  = value  
          mintimestamp = value  
          maxtimestamp = value  
          minnumber    = value, applies only if event.number is present  
          maxnmumber   = value, applies only if event.number is present  
         
        See also FT_READ_EVENT, FT_WRITE_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_filter_event.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_filter_event", *args, **kwargs)
