from spm._runtime import Runtime


def ft_poll_buffer(*args, **kwargs):
    r"""
      FT_POLL_BUFFER is deprecated.  
         
        Please use FT_READ_DATA and FT_READ_EVENT with the  'blocking' and  
        the 'timeout' options.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_poll_buffer.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_poll_buffer", *args, **kwargs)
