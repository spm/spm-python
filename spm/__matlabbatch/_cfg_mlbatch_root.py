from spm.__wrapper__ import Runtime


def _cfg_mlbatch_root(*args, **kwargs):
  """  function c = cfg_mlbatch_root  
    The root node of a matlabbatch configuration. This file is called by  
    cfg_util when initialising its internal data structure.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_mlbatch_root.m)
  """

  return Runtime.call("cfg_mlbatch_root", *args, **kwargs)
