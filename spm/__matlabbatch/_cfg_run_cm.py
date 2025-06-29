from spm._runtime import Runtime


def _cfg_run_cm(*args, **kwargs):
    """
      function cm = cfg_run_cm(cm, job)  
        Run a module and return its output. Should really become a method of  
        cfg_exbranch classes.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_run_cm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_run_cm", *args, **kwargs)
