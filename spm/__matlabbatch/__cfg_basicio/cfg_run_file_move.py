from spm.__wrap__ import _Runtime


def cfg_run_file_move(*args, **kwargs):
  """  Move files to another directory or delete them, if no directory is  
    specified. Special treatment to move .img/.hdr/.mat pairs of files  
    together.  
     
    This code is part of a batch job configuration system for MATLAB. See  
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_file_move.m)
  """

  return _Runtime.call("cfg_run_file_move", *args, **kwargs)
