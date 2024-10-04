from spm.__wrap__ import _Runtime


def cfg_vout_runjobs(*args, **kwargs):
  """  Return dependency to jobfiles, if files are to be saved.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_runjobs.m)
  """

  return _Runtime.call("cfg_vout_runjobs", *args, **kwargs)
