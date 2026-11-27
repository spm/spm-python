from spm._runtime import Runtime


def cfg_basicio_rewrite(*args, **kwargs):
    r"""
      Rewrite job to conform to new submenu structure of BasicIO  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_basicio/cfg_basicio_rewrite.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_basicio_rewrite", *args, **kwargs)
