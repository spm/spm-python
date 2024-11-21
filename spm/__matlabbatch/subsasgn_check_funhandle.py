from spm.__wrapper__ import Runtime


def subsasgn_check_funhandle(*args, **kwargs):
    """
      function sts = subsasgn_check_funhandle(val)  
        Return true if val is either empty, or a function or function handle.  
        One could also check for nargin == 1 and nargout == 1.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/subsasgn_check_funhandle.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("subsasgn_check_funhandle", *args, **kwargs)
