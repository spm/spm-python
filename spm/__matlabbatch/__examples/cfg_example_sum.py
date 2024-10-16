from spm.__wrapper__ import Runtime


def cfg_example_sum(*args, **kwargs):
  """  Example script that creates an cfg_exbranch to sum two numbers. The  
    inputs are entered as vector, the output is just a single  
    number. This function differs from cfg_example_add2 (except from names)  
    only in the specification of input1.num.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_sum.m)
  """

  return Runtime.call("cfg_example_sum", *args, **kwargs)
