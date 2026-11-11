from spm._runtime import Runtime


def ft_flush_data(*args, **kwargs):
    r"""
      FT_FLUSH_DATA removes all data from the data queue  
         
        Use as  
          ft_flush_data(filename, ...)  
         
        See also FT_FLUSH_HEADER, FT_FLUSH_EVENT  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_flush_data.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_flush_data", *args, **kwargs, nargout=0)
