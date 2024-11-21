from spm.__wrapper__ import Runtime


def ft_destroy_buffer(*args, **kwargs):
    """
      FT_DESTROY_BUFFER stops the thread with the TCP server attached to  
        the local MATLAB instance and removes all data from memory.  
         
        Use as  
          ft_destroy_buffer  
         
        See also FT_CREATE_BUFFER  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_destroy_buffer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_destroy_buffer", *args, **kwargs, nargout=0)
