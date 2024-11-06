from spm.__wrapper__ import Runtime


def cfg_run_file_move(*args, **kwargs):
    """
      Move files to another directory or delete them, if no directory is  
        specified. Special treatment to move .img/.hdr/.mat pairs of files  
        together.  
         
        This code is part of a batch job configuration system for MATLAB. See  
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_run_file_move.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_run_file_move", *args, **kwargs)
