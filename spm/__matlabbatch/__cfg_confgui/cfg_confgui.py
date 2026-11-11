from spm._runtime import Runtime


def cfg_confgui(*args, **kwargs):
    r"""
      This function describes the user defined fields for each kind of  
        cfg_item and their layout in terms of cfg_items. Thus, the  
        configuration system can be used to generate code for new configuration  
        files itself.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_confgui/cfg_confgui.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_confgui", *args, **kwargs)
