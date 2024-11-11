from spm.__wrapper__ import Runtime


def cfg_ui_util(*args, **kwargs):
    """
     CFG_UI_UTIL utility functions for displaying job, module and item values  
        This function is a collection of utility functions to display a job,  
        module or data summary. It also handles all value display and editing for  
        a particular item.  
         
        This code is part of a batch job configuration system for MATLAB. See  
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_ui_util.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_ui_util", *args, **kwargs)
