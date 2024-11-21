from spm.__wrapper__ import Runtime


def ft_compile_standalone(*args, **kwargs):
    """
      FT_COMPILE_STANDALONE compiles the FieldTrip functions along with  
        the standalone entry function into a compiled executable.  
         
        The compiled executable includes  
         - all main FieldTrip m-files  
         - all main FieldTrip m-files dependencies for as long as these  
           dependencies are in the fieldtrip modules and external toolboxes  
           on the path, MATLAB built-in, or toolbox/(stats/images/signal)  
           functions  
         
        See also FT_STANDALONE, FT_COMPILE_MEX  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/ft_compile_standalone.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("ft_compile_standalone", *args, **kwargs, nargout=0)
