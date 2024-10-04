from spm.__wrap__ import _Runtime


def _cfg_ui_getListboxTop(*args, **kwargs):
  """  Get a safe value for ListboxTop property while keeping previous settings  
    if possible.  
    obj     handle of Listbox object  
    val     new Value property  
    maxval  new number of lines in obj  
     
    This code is part of a batch job configuration system for MATLAB. See   
         help matlabbatch  
    for a general overview.  
   _______________________________________________________________________  
    Copyright (C) 2007 Freiburg Brain Imaging  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_ui_getListboxTop.m)
  """

  return _Runtime.call("cfg_ui_getListboxTop", *args, **kwargs)
