from spm.__wrap__ import _Runtime


def cfg_run_assignin(*args, **kwargs):
  """  Assign the value of job.output to a workspace variable job.name.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_assignin.m)
  """

  return _Runtime.call("cfg_run_assignin", *args, **kwargs, nargout=0)
