from spm.__wrap__ import _Runtime


def _cfg_textfill(*args, **kwargs):
  """  function str = cfg_textfill(obj, left, right)  
    Fill a text object, so that the left part is left justified and the  
    right part right justified. If tflag is set, try to fit text in widget  
    by truncating right until at least 5 characters are displayed.  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_textfill.m)
  """

  return _Runtime.call("cfg_textfill", *args, **kwargs)
