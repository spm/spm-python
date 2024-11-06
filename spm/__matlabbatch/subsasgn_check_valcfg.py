from spm.__wrapper__ import Runtime


def subsasgn_check_valcfg(*args, **kwargs):
    """
      function sts = subsasgn_check_valcfg(subs,val,num)  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/subsasgn_check_valcfg.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("subsasgn_check_valcfg", *args, **kwargs)
