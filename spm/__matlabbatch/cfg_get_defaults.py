from spm.__wrap__ import _Runtime


def cfg_get_defaults(*args, **kwargs):
  """  function varargout = cfg_get_defaults(defspec, varargin)  
    Get/set defaults for various properties of matlabbatch utilities.  
    The values can be modified permanently by editing the file  
    private/cfg_mlbatch_defaults.m   
    or for the current MATLAB session by calling  
    cfg_get_defaults(defspec, defval).  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_get_defaults.m)
  """

  return _Runtime.call("cfg_get_defaults", *args, **kwargs)
