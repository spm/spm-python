from spm.__wrapper__ import Runtime


def cfg_check_assignin(*args, **kwargs):
    """
      Check whether the name entered for the workspace variable is a proper  
        variable name.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_check_assignin.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_check_assignin", *args, **kwargs)
