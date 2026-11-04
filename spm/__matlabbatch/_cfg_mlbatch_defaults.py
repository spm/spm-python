from spm._runtime import Runtime


def _cfg_mlbatch_defaults(*args, **kwargs):
    r"""
      function cfg_defaults = cfg_mlbatch_defaults  
        This file contains defaults that control the behaviour and appearance   
        of matlabbatch.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_mlbatch_defaults.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_mlbatch_defaults", *args, **kwargs)
