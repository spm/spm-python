from spm._runtime import Runtime


def cfg_vout_mkdir(*args, **kwargs):
    r"""
      Define virtual outputs for cfg_run_mkdir. The directory name can either  
        be assigned to a cfg_files directory input or to a evaluated cfg_entry.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_basicio/cfg_vout_mkdir.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_vout_mkdir", *args, **kwargs)
