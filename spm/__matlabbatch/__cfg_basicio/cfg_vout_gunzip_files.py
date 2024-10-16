from spm.__wrapper__ import Runtime


def cfg_vout_gunzip_files(*args, **kwargs):
  """  Define virtual outputs for "Gunzip Files". File names can either be  
    assigned to a cfg_files input or to a evaluated cfg_entry.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_gunzip_files.m)
  """

  return Runtime.call("cfg_vout_gunzip_files", *args, **kwargs)
