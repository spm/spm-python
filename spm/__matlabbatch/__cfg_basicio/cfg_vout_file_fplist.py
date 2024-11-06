from spm.__wrapper__ import Runtime


def cfg_vout_file_fplist(*args, **kwargs):
    """
      function dep = cfg_vout_file_fplist(job)  
         
        Virtual outputs for cfg_run_file_fplist. Struct with fields .files and  
        .dirs. See help on cfg_getfile.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_fplist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_vout_file_fplist", *args, **kwargs)
