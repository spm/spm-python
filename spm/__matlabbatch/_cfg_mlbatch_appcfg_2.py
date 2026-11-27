from spm._runtime import Runtime


def _cfg_mlbatch_appcfg_2(*args, **kwargs):
    r"""
      Add BasicIO to applications list of cfg_util. This file is an example how  
        to add your own application configuration to cfg_util. To add an  
        application, create a file called cfg_mlbatch_appcfg.m in the application  
        folder and add this folder to the MATLAB path. cfg_util will look for  
        files with the exact name cfg_mlbatch_appcfg.m and run all of them in  
        order of their occurrence on the path.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_mlbatch_appcfg_2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_mlbatch_appcfg", *args, **kwargs)
