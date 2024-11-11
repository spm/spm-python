from spm.__wrapper__ import Runtime


def _cfg_util_persistent(*args, **kwargs):
    """
     CFG_UTIL_PERSISTENT - store persistent variables for cfg_util  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_util_persistent.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_util_persistent", *args, **kwargs)
