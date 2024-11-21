from spm.__wrapper__ import Runtime


def cfg_example_master(*args, **kwargs):
    """
      Master file that collects the cfg_exbranches in conceptually similar  
        groups.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_master.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_example_master", *args, **kwargs)
