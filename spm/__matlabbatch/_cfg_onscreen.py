from spm._runtime import Runtime


def _cfg_onscreen(*args, **kwargs):
    r"""
      Move figure on the screen containing the mouse  
           cfg_onscreen(fg) - move figure fg on the screen containing the mouse  
           pos = cfg_onscreen(fg) - compute position of figure, do not move it  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_onscreen.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_onscreen", *args, **kwargs)
