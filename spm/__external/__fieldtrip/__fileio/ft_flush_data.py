from spm.__wrapper__ import Runtime


def ft_flush_data(*args, **kwargs):
    """
      FT_FLUSH_DATA removes all data from the data queue  
         
        Use as  
          ft_flush_data(filename, ...)  
         
        See also FT_FLUSH_HEADER, FT_FLUSH_EVENT  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/ft_flush_data.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_flush_data", *args, **kwargs, nargout=0)
