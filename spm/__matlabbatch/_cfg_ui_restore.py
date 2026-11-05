from spm._runtime import Runtime


def _cfg_ui_restore(*args, **kwargs):
    r"""
     CFG_UI_RESTORE Restore state of properties  
        CFG_UI_RESTORE(en) restores property values that were disabled by  
        CFG_UI_DISABLE.  
         
        See also CFG_UI_DISABLE.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_ui_restore.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_ui_restore", *args, **kwargs, nargout=0)
