from spm.__wrapper__ import Runtime


def cfg_load_vars(*args, **kwargs):
    """
      Load a .mat file, and return its contents via output dependencies.  
        varargout = cfg_load_vars(cmd, varargin)  
        where cmd is one of  
        'run'      - out = cfg_load_vars('run', job)  
                     Run a job, and return its output argument  
        'vout'     - dep = cfg_load_vars('vout', job)  
                     Create a virtual output for each requested variable. If  
                     "all variables" are requested, only one output will be  
                     generated.  
        'check'    - str = cfg_load_vars('check', subcmd, subjob)  
                     'isvarname' - check whether the entered string is a valid  
                                   MATLAB variable name. This does not check  
                                   whether the variable is present in the .mat file.  
        'defaults' - defval = cfg_load_vars('defaults', key)  
                     No defaults.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_load_vars.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_load_vars", *args, **kwargs)
