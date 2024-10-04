from spm.__wrap__ import _Runtime


def _cfg_run_cm(*args, **kwargs):
  """  function cm = cfg_run_cm(cm, job)  
    Run a module and return its output. Should really become a method of  
    cfg_exbranch classes.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_run_cm.m)
  """

  return _Runtime.call("cfg_run_cm", *args, **kwargs)
