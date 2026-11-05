from spm._runtime import Runtime


def _cfg_eval_valedit(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_eval_valedit.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_eval_valedit", *args, **kwargs)
