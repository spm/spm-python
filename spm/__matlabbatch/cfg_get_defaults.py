from spm.__wrapper__ import Runtime


def cfg_get_defaults(*args, **kwargs):
    """
      function varargout = cfg_get_defaults(defspec, varargin)  
        Get/set defaults for various properties of matlabbatch utilities.  
        The values can be modified permanently by editing the file  
        private/cfg_mlbatch_defaults.m   
        or for the current MATLAB session by calling  
        cfg_get_defaults(defspec, defval).  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_get_defaults.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_get_defaults", *args, **kwargs)
