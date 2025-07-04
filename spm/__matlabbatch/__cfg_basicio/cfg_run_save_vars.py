from spm._runtime import Runtime


def cfg_run_save_vars(*args, **kwargs):
    """
      Save input variables to .mat file - either as a struct array, or as  
        individual variables.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_save_vars.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_run_save_vars", *args, **kwargs)
