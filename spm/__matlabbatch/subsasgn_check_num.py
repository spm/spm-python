from spm._runtime import Runtime


def subsasgn_check_num(*args, **kwargs):
    r"""
      function sts = subsasgn_check_num(val)  
        Check, whether a num value is a numeric 2-vector, denoting a  
        minimum/maximum number of elements. val(1) must be >= 0 and   
        val(2) >= val(1).   
        This function is called for all num fields, except those in cfg_entry  
        objects.   
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/subsasgn_check_num.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("subsasgn_check_num", *args, **kwargs)
