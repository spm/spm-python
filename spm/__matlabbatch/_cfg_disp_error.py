from spm.__wrap__ import _Runtime


def _cfg_disp_error(*args, **kwargs):
  """  function varargout = cfg_disp_error(errstruct)  
     
    Display a condensed version of a MATLAB error without rethrowing it.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_disp_error.m)
  """

  return _Runtime.call("cfg_disp_error", *args, **kwargs)
