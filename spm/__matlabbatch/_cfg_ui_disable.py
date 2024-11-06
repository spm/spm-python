from spm.__wrapper__ import Runtime


def _cfg_ui_disable(*args, **kwargs):
    """
     CFG_UI_DISABLE Disable properties  
        en = CFG_UI_DISABLE(hObject, property) disables property in all children  
        of hObject, returning their handles in en.c and previous state in cell  
        list en.en. CFG_UI_RESTORE(en) can be used to restore the property to  
        their original setting.  
        Property must be a property that has the values 'on' (enabled) or 'off'  
        (disabled).  
         
        See also CFG_UI_RESTORE.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_ui_disable.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_ui_disable", *args, **kwargs)
