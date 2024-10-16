from spm.__wrapper__ import Runtime


def _cfg_onscreen(*args, **kwargs):
  """  Move figure on the screen containing the mouse  
       cfg_onscreen(fg) - move figure fg on the screen containing the mouse  
       pos = cfg_onscreen(fg) - compute position of figure, do not move it  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_onscreen.m)
  """

  return Runtime.call("cfg_onscreen", *args, **kwargs)
