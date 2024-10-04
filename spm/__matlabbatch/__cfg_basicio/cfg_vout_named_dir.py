from spm.__wrap__ import _Runtime


def cfg_vout_named_dir(*args, **kwargs):
  """  Define virtual outputs for cfg_run_named_dir. Dir names can either be  
    assigned to a cfg_dirs input or to a evaluated cfg_entry. Dir indices  
    can be assigned to any numeric or evaluated cfg_entry item.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_named_dir.m)
  """

  return _Runtime.call("cfg_vout_named_dir", *args, **kwargs)
