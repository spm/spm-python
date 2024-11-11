from spm.__wrapper__ import Runtime


def cfg_run_file_fplist(*args, **kwargs):
    """
      function out = cfg_run_file_fplist(job)  
         
        Select files non-interactively using cfg_getfile('FPList',...) or  
        cfg_getfile('FPListRec',...).  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_file_fplist.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_run_file_fplist", *args, **kwargs)
