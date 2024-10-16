from spm.__wrapper__ import Runtime


def cfg_vout_named_input(*args, **kwargs):
  """  Define virtual output for cfg_run_named_input. This input can be assigned  
    to any cfg_entry input item.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_named_input.m)
  """

  return Runtime.call("cfg_vout_named_input", *args, **kwargs)
