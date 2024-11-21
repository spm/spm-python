from spm.__wrapper__ import Runtime


def cfg_load_jobs(*args, **kwargs):
    """
      function newjobs = cfg_load_jobs(job)  
         
        Load a list of possible job files, return a cell list of jobs.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_load_jobs.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_load_jobs", *args, **kwargs)
