from spm.__wrapper__ import Runtime


def cfg_vout_fileparts(*args, **kwargs):
    """
      Define virtual outputs for cfg_run_fileparts. The path names can either  
        be assigned to a cfg_files input or to an evaluated cfg_entry. File names  
        and extensions can only be assigned to an evaluated cfg_entry.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_fileparts.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_vout_fileparts", *args, **kwargs)
