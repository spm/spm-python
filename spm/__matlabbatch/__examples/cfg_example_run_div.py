from spm.__wrap__ import _Runtime


def cfg_example_run_div(*args, **kwargs):
  """  Example function that returns the mod and rem of two numbers given in  
    job.a and job.b in out.mod and out.rem.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_run_div.m)
  """

  return _Runtime.call("cfg_example_run_div", *args, **kwargs)
