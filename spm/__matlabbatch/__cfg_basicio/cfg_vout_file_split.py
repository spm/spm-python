from spm._runtime import Runtime


def cfg_vout_file_split(*args, **kwargs):
    """
      Define virtual outputs for cfg_run_file_split. File names can either be  
        assigned to a cfg_files input or to a evaluated cfg_entry.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_split.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_vout_file_split", *args, **kwargs)
