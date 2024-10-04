from spm.__wrap__ import _Runtime


def cfg_run_gzip_files(*args, **kwargs):
  """  Run gzip on a list of files.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_gzip_files.m)
  """

  return _Runtime.call("cfg_run_gzip_files", *args, **kwargs)
