from spm._runtime import Runtime


def cfg_vout_gzip_files(*args, **kwargs):
    """
      Define virtual outputs for "Gzip Files". File names can either be  
        assigned to a cfg_files input or to a evaluated cfg_entry.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_gzip_files.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_vout_gzip_files", *args, **kwargs)
