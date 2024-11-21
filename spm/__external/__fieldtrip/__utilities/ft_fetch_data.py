from spm.__wrapper__ import Runtime


def ft_fetch_data(*args, **kwargs):
    """
      FT_FETCH_DATA mimics the behavior of FT_READ_DATA, but for a FieldTrip  
        raw data structure instead of a file on disk.  
         
        Use as  
          [dat] = ft_fetch_data(data, ...)  
         
        See also FT_READ_DATA, FT_FETCH_HEADER, FT_FETCH_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_fetch_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_fetch_data", *args, **kwargs)
