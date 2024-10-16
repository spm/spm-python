from spm.__wrapper__ import Runtime


def cfg_run_cd(*args, **kwargs):
  """  Make a directory and return its path in out.dir{1}.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_cd.m)
  """

  return Runtime.call("cfg_run_cd", *args, **kwargs, nargout=0)
