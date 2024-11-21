from spm.__wrapper__ import Runtime


def cfg_mlbatch_appcfg(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_mlbatch_appcfg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_mlbatch_appcfg", *args, **kwargs)
