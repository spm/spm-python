from spm.__wrap__ import _Runtime


def cfg_run_file_fplist(*args, **kwargs):
  """  function out = cfg_run_file_fplist(job)  
     
    Select files non-interactively using cfg_getfile('FPList',...) or  
    cfg_getfile('FPListRec',...).  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_file_fplist.m)
  """

  return _Runtime.call("cfg_run_file_fplist", *args, **kwargs)
