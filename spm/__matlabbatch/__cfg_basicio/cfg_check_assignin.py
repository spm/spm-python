from spm.__wrap__ import _Runtime


def cfg_check_assignin(*args, **kwargs):
  """  Check whether the name entered for the workspace variable is a proper  
    variable name.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_check_assignin.m)
  """

  return _Runtime.call("cfg_check_assignin", *args, **kwargs)
