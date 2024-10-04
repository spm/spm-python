from spm.__wrap__ import _Runtime


def cfg_load_jobs(*args, **kwargs):
  """  function newjobs = cfg_load_jobs(job)  
     
    Load a list of possible job files, return a cell list of jobs.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_load_jobs.m)
  """

  return _Runtime.call("cfg_load_jobs", *args, **kwargs)
