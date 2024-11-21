from spm.__wrapper__ import Runtime


def cfg_basicio_rewrite(*args, **kwargs):
    """
      Rewrite job to conform to new submenu structure of BasicIO  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_basicio_rewrite.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_basicio_rewrite", *args, **kwargs)
