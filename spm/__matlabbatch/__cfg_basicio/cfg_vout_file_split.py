from spm.__wrap__ import _Runtime


def cfg_vout_file_split(*args, **kwargs):
  """  Define virtual outputs for cfg_run_file_split. File names can either be  
    assigned to a cfg_files input or to a evaluated cfg_entry.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_split.m)
  """

  return _Runtime.call("cfg_vout_file_split", *args, **kwargs)
