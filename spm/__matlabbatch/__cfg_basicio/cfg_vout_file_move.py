from spm.__wrapper__ import Runtime


def cfg_vout_file_move(*args, **kwargs):
    """
      Define virtual output for cfg_run_move_file. Output can be passed on to  
        either a cfg_files or an evaluated cfg_entry.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/cfg_vout_file_move.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_vout_file_move", *args, **kwargs)
