from spm.__wrapper__ import Runtime


def cfg_vout_named_dir(*args, **kwargs):
    """
      Define virtual outputs for cfg_run_named_dir. Dir names can either be  
        assigned to a cfg_dirs input or to a evaluated cfg_entry. Dir indices  
        can be assigned to any numeric or evaluated cfg_entry item.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_named_dir.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_vout_named_dir", *args, **kwargs)
