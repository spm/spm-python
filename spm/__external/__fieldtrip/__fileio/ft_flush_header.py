from spm._runtime import Runtime


def ft_flush_header(*args, **kwargs):
    r"""
      FT_FLUSH_HEADER removes the header information from the data queue  
        this also removes all data associated with the specific header.  
         
        Use as  
          ft_flush_header(filename, ...)  
         
        See also FT_FLUSH_DATA, FT_FLUSH_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_flush_header.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_flush_header", *args, **kwargs, nargout=0)
