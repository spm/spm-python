from spm.__wrapper__ import Runtime


def ft_fetch_event(*args, **kwargs):
    """
      FT_FETCH_EVENT mimics the behavior of FT_READ_EVENT, but for a FieldTrip  
        raw data structure instead of a file on disk.  
         
        Use as  
          event = ft_fetch_event(data)  
         
        See also FT_READ_EVENT, FT_FETCH_HEADER, FT_FETCH_DATA  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_fetch_event.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_fetch_event", *args, **kwargs)
