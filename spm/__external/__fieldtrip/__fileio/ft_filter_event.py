from spm.__wrapper__ import Runtime


def ft_filter_event(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_filter_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_filter_event", *args, **kwargs)
