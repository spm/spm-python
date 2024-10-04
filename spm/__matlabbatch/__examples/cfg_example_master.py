from spm.__wrap__ import _Runtime


def cfg_example_master(*args, **kwargs):
  """  Master file that collects the cfg_exbranches in conceptually similar  
    groups.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_master.m)
  """

  return _Runtime.call("cfg_example_master", *args, **kwargs)
