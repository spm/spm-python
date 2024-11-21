from spm.__wrapper__ import Runtime


def cfg_struct2cfg(*args, **kwargs):
    """
      Import a config structure into a matlabbatch class tree. Input structures  
        are those generated from the configuration editor, cfg2struct methods or  
        spm_jobman config structures.  
         
        The layout of the configuration tree and the types of configuration items  
        have been kept compatible to a configuration system and job manager  
        implementation in SPM5 (Statistical Parametric Mapping, Copyright (C)  
        2005 Wellcome Department of Imaging Neuroscience). This code has been  
        completely rewritten based on an object oriented model of the  
        configuration tree.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_struct2cfg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_struct2cfg", *args, **kwargs)
