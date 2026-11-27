from spm._runtime import Runtime


def ft_preamble(*args, **kwargs):
    r"""
      FT_PREAMBLE is a helper function that is included in many of the FieldTrip  
        functions and which takes care of some general settings and operations at the  
        begin of the function.  
         
        This ft_preamble m-file is a function, but internally it executes a  
        number of private scripts in the callers workspace. This allows the  
        private script to access the variables in the callers workspace and  
        behave as if the script were included as a header file in C-code.  
         
        See also FT_POSTAMBLE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/ft_preamble.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ft_preamble", *args, **kwargs, nargout=0)
