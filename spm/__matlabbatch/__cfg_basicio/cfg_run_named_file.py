from spm.__wrap__ import _Runtime


def cfg_run_named_file(*args, **kwargs):
  """  Return selected files as separate output arguments.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_named_file.m)
  """

  return _Runtime.call("cfg_run_named_file", *args, **kwargs)
