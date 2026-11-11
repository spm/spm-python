from spm._runtime import Runtime


def _cfg_ui_getListboxTop(*args, **kwargs):
    r"""
      Get a safe value for ListboxTop property while keeping previous settings  
        if possible.  
        obj     handle of Listbox object  
        val     new Value property  
        maxval  new number of lines in obj  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_ui_getListboxTop.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_ui_getListboxTop", *args, **kwargs)
