from spm.__wrapper__ import Runtime


def ft_fetch_header(*args, **kwargs):
    """
      FT_FETCH_HEADER mimics the behavior of FT_READ_HEADER, but for a FieldTrip  
        raw data structure instead of a file on disk.  
         
        Use as  
          hdr = ft_fetch_header(data)  
         
        See also FT_READ_HEADER, FT_FETCH_DATA, FT_FETCH_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_fetch_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_fetch_header", *args, **kwargs)
