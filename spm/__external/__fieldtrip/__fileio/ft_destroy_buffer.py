from spm._runtime import Runtime


def ft_destroy_buffer(*args, **kwargs):
    r"""
      FT_DESTROY_BUFFER stops the thread with the TCP server attached to  
        the local MATLAB instance and removes all data from memory.  
         
        Use as  
          ft_destroy_buffer  
         
        See also FT_CREATE_BUFFER  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/fileio/ft_destroy_buffer.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_destroy_buffer", *args, **kwargs, nargout=0)
