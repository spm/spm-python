from spm.__wrapper__ import Runtime


def cfg_vout_file_filter(*args, **kwargs):
    """
      Define virtual outputs for cfg_vout_file_filter. The file names can either  
        be assigned to a cfg_files input or to a evaluated cfg_entry.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_filter.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_vout_file_filter", *args, **kwargs)
