from spm._runtime import Runtime


def ft_fetch_header(*args, **kwargs):
    r"""
      FT_FETCH_HEADER mimics the behavior of FT_READ_HEADER, but for a FieldTrip  
        raw data structure instead of a file on disk.  
         
        Use as  
          hdr = ft_fetch_header(data)  
         
        See also FT_READ_HEADER, FT_FETCH_DATA, FT_FETCH_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_fetch_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_fetch_header", *args, **kwargs)
