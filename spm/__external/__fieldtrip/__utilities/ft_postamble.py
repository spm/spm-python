from spm.__wrapper__ import Runtime


def ft_postamble(*args, **kwargs):
    """
      FT_POSTAMBLE is a helper function that is included in many of the FieldTrip  
        functions and which takes care of some general settings and operations at the end  
        of the function.  
         
        This ft_postamble m-file is a function, but internally it executes a number of  
        private scripts in the callers workspace. This allows the private script to access  
        the variables in the callers workspace and behave as if the script were included as  
        a header file in C-code.  
         
        See also FT_PREAMBLE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_postamble.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_postamble", *args, **kwargs, nargout=0)
