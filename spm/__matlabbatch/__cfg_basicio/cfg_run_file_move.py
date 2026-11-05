from spm._runtime import Runtime


def cfg_run_file_move(*args, **kwargs):
    r"""
      Move files to another directory or delete them, if no directory is  
        specified. Special treatment to move .img/.hdr/.mat pairs of files  
        together.  
         
        This code is part of a batch job configuration system for MATLAB. See  
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_basicio/cfg_run_file_move.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_run_file_move", *args, **kwargs)
