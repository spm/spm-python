from spm.__wrapper__ import Runtime


def _cfg_ui_restore(*args, **kwargs):
    """
     CFG_UI_RESTORE Restore state of properties  
        CFG_UI_RESTORE(en) restores property values that were disabled by  
        CFG_UI_DISABLE.  
         
        See also CFG_UI_DISABLE.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_ui_restore.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_ui_restore", *args, **kwargs, nargout=0)
