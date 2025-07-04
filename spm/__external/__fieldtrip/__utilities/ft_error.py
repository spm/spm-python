from spm._runtime import Runtime


def ft_error(*args, **kwargs):
    """
      FT_ERROR prints an error message on screen, just like the standard ERROR function.  
         
        Use as  
          ft_error(...)  
        with arguments similar to fprintf, or  
          ft_error(msgId, ...)  
        with arguments similar to error.  
         
        See also FT_ERROR, FT_WARNING, FT_NOTICE, FT_INFO, FT_DEBUG, ERROR, WARNING  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_error.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_error", *args, **kwargs)
