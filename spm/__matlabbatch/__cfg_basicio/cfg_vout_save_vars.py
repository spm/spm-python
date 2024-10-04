from spm.__wrap__ import _Runtime


def cfg_vout_save_vars(*args, **kwargs):
  """  Define virtual output for cfg_run_save_vars. Output can be passed on to  
    either a cfg_file or an evaluated cfg_entry.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_save_vars.m)
  """

  return _Runtime.call("cfg_vout_save_vars", *args, **kwargs)
