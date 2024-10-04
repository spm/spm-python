from spm.__wrap__ import _Runtime


def _cfg_mlbatch_defaults(*args, **kwargs):
  """  function cfg_defaults = cfg_mlbatch_defaults  
    This file contains defaults that control the behaviour and appearance   
    of matlabbatch.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_mlbatch_defaults.m)
  """

  return _Runtime.call("cfg_mlbatch_defaults", *args, **kwargs)
