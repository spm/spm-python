from spm._runtime import Runtime


def cfg_run_runjobs(*args, **kwargs):
    """
      Initialise, fill, save and run a job with repeated inputs.  
        To make use of possible parallel execution of independent jobs, all  
        repeated jobs are filled first and (if successfully filled) run as one  
        large job.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_runjobs.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_run_runjobs", *args, **kwargs)
