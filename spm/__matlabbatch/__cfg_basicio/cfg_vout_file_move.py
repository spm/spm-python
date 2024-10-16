from spm.__wrapper__ import Runtime


def cfg_vout_file_move(*args, **kwargs):
  """  Define virtual output for cfg_run_move_file. Output can be passed on to  
    either a cfg_files or an evaluated cfg_entry.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_move.m)
  """

  return Runtime.call("cfg_vout_file_move", *args, **kwargs)
