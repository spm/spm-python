from spm.__wrap__ import _Runtime


def cfg_vout_file_fplist(*args, **kwargs):
  """  function dep = cfg_vout_file_fplist(job)  
     
    Virtual outputs for cfg_run_file_fplist. Struct with fields .files and  
    .dirs. See help on cfg_getfile.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_fplist.m)
  """

  return _Runtime.call("cfg_vout_file_fplist", *args, **kwargs)
