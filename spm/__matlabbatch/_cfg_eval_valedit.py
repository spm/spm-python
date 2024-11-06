from spm.__wrapper__ import Runtime


def _cfg_eval_valedit(*args, **kwargs):
    """
      Helper function to evaluate GUI inputs in MATLAB workspace  
        FORMAT [val, sts] = cfg_eval_valedit(str)  
        Evaluates GUI inputs in MATLAB 'base' workspace. Results are returned  
        in val. Expressions in str can be either a pure rhs argument, or a set  
        of commands that assign to a workspace variable named 'val'. If  
        unsuccessful, sts is false and a message window is displayed.   
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_eval_valedit.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_eval_valedit", *args, **kwargs)
