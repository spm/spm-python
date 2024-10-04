from spm.__wrap__ import _Runtime


def cfg_example_run_add2(*args, **kwargs):
  """  Example function that returns the sum of two numbers given in job.a in  
    out. The output is referenced as out(1), this is defined in  
    cfg_example_vout_add2.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_run_add2.m)
  """

  return _Runtime.call("cfg_example_run_add2", *args, **kwargs)
