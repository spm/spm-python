from spm._runtime import Runtime


def cfg_load_jobs(*args, **kwargs):
    r"""
      function newjobs = cfg_load_jobs(job)  
         
        Load a list of possible job files, return a cell list of jobs.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_load_jobs.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_load_jobs", *args, **kwargs)
