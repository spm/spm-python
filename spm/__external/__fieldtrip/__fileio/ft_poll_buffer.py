from spm.__wrapper__ import Runtime


def ft_poll_buffer(*args, **kwargs):
    """
      FT_POLL_BUFFER is deprecated.  
         
        Please use FT_READ_DATA and FT_READ_EVENT with the  'blocking' and  
        the 'timeout' options.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_poll_buffer.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_poll_buffer", *args, **kwargs)
