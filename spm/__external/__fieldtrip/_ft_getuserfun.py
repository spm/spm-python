from spm.__wrapper__ import Runtime


def _ft_getuserfun(*args, **kwargs):
    """
      FT_GETUSERFUN will search the MATLAB path for a function with the  
        appropriate name, and return a function handle to the function.  
        Considered are, in this order:  
         - the name itself, i.e. you get exactly the same func back as you put in;  
         - the name with the specified prefix;  
         - the name with 'ft_' and the specified prefix.  
         
        For example, calling FT_GETUSERFUN('general', 'trialfun') might return a  
        function named 'general', 'trialfun_general', or 'ft_trialfun_general',  
        whichever of those is found first and is not a compatibility wrapper.  
         
        func can be a function handle, in which case it is returned as-is.  
         
        If no appropriate function is found, the empty array [] will be returned.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/ft_getuserfun.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_getuserfun", *args, **kwargs)
