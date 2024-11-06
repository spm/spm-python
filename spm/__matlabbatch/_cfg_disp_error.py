from spm.__wrapper__ import Runtime


def _cfg_disp_error(*args, **kwargs):
    """
      function varargout = cfg_disp_error(errstruct)  
         
        Display a condensed version of a MATLAB error without rethrowing it.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_disp_error.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_disp_error", *args, **kwargs)
