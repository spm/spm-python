from spm.__wrapper__ import Runtime


def subsasgn_check_num(*args, **kwargs):
    """
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
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/subsasgn_check_num.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("subsasgn_check_num", *args, **kwargs)
