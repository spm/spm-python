from spm.__wrapper__ import Runtime


def cfg_run_call_matlab(*args, **kwargs):
    """
      A generic interface to call any MATLAB function through the batch system  
        and make its output arguments available as dependencies.  
        varargout = cfg_run_call_matlab(cmd, varargin)  
        where cmd is one of  
        'run'      - out = cfg_run_call_matlab('run', job)  
                     Run the function, and return the specified output arguments  
        'vout'     - dep = cfg_run_call_matlab('vout', job)  
                     Return dependencies as specified via the output cfg_repeat.  
        'check'    - str = cfg_run_call_matlab('check', subcmd, subjob)  
                     Examine a part of a fully filled job structure. Return an empty  
                     string if everything is ok, or a string describing the check  
                     error. subcmd should be a string that identifies the part of  
                     the configuration to be checked.  
        'defaults' - defval = cfg_run_call_matlab('defaults', key)  
                     Retrieve defaults value. key must be a sequence of dot  
                     delimited field names into the internal def struct which is  
                     kept in function local_def. An error is returned if no  
                     matching field is found.  
                     cfg_run_call_matlab('defaults', key, newval)  
                     Set the specified field in the internal def struct to a new  
                     value.  
        Application specific code needs to be inserted at the following places:  
        'run'      - main switch statement: code to compute the results, based on  
                     a filled job  
        'vout'     - main switch statement: code to compute cfg_dep array, based  
                     on a job structure that has all leafs, but not necessarily  
                     any values filled in  
        'check'    - create and populate switch subcmd switchyard  
        'defaults' - modify initialisation of defaults in subfunction local_defs  
        Callbacks can be constructed using anonymous function handles like this:  
        'run'      - @(job)cfg_run_call_matlab('run', job)  
        'vout'     - @(job)cfg_run_call_matlab('vout', job)  
        'check'    - @(job)cfg_run_call_matlab('check', 'subcmd', job)  
        'defaults' - @(val)cfg_run_call_matlab('defaults', 'defstr', val{:})  
                     Note the list expansion val{:} - this is used to emulate a  
                     varargin call in this function handle.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_call_matlab.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_run_call_matlab", *args, **kwargs)
