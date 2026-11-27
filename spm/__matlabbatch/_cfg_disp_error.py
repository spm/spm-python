from spm._runtime import Runtime


def _cfg_disp_error(*args, **kwargs):
    r"""
      function varargout = cfg_disp_error(errstruct)  
         
        Display a condensed version of a MATLAB error without rethrowing it.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/private/cfg_disp_error.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_disp_error", *args, **kwargs)
