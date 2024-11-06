from spm.__wrapper__ import Runtime


def cfg_confgui(*args, **kwargs):
    """
      This function describes the user defined fields for each kind of  
        cfg_item and their layout in terms of cfg_items. Thus, the  
        configuration system can be used to generate code for new configuration  
        files itself.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_confgui/cfg_confgui.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_confgui", *args, **kwargs)
