from spm.__wrapper__ import Runtime


def ft_flush_header(*args, **kwargs):
    """
      FT_FLUSH_HEADER removes the header information from the data queue  
        this also removes all data associated with the specific header.  
         
        Use as  
          ft_flush_header(filename, ...)  
         
        See also FT_FLUSH_DATA, FT_FLUSH_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_flush_header.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_flush_header", *args, **kwargs, nargout=0)
