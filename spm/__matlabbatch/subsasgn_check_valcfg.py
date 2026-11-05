from spm._runtime import Runtime


def subsasgn_check_valcfg(*args, **kwargs):
    r"""
      function sts = subsasgn_check_valcfg(subs,val,num)  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/subsasgn_check_valcfg.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("subsasgn_check_valcfg", *args, **kwargs)
