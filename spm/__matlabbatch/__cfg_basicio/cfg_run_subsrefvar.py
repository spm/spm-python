from spm.__wrapper__ import Runtime


def cfg_run_subsrefvar(*args, **kwargs):
    """
      Template function to implement callbacks for an cfg_exbranch. The calling  
        syntax is  
        varargout = cfg_run_subsrefvar(cmd, varargin)  
        where cmd is one of  
        'run'      - out = cfg_run_subsrefvar('run', job)  
                     Run a job, and return its output argument  
        'vout'     - dep = cfg_run_subsrefvar('vout', job)  
                     Examine a job structure with all leafs present and return an  
                     array of cfg_dep objects.  
        'check'    - str = cfg_run_subsrefvar('check', subcmd, subjob)  
                     Examine a part of a fully filled job structure. Return an empty  
                     string if everything is ok, or a string describing the check  
                     error. subcmd should be a string that identifies the part of  
                     the configuration to be checked.  
        'defaults' - defval = cfg_run_subsrefvar('defaults', key)  
                     Retrieve defaults value. key must be a sequence of dot  
                     delimited field names into the internal def struct which is  
                     kept in function local_def. An error is returned if no  
                     matching field is found.  
                     cfg_run_subsrefvar('defaults', key, newval)  
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
        'run'      - @(job)cfg_run_subsrefvar('run', job)  
        'vout'     - @(job)cfg_run_subsrefvar('vout', job)  
        'check'    - @(job)cfg_run_subsrefvar('check', 'subcmd', job)  
        'defaults' - @(val)cfg_run_subsrefvar('defaults', 'defstr', val{:})  
                     Note the list expansion val{:} - this is used to emulate a  
                     varargin call in this function handle.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_subsrefvar.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_run_subsrefvar", *args, **kwargs)
