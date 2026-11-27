from spm._runtime import Runtime


def cfg_tropts(*args, **kwargs):
    r"""
      function tropts = cfg_tropts(stopspec, clvl, mlvl, cnt, mcnt, dflag)  
        This function is a shorthand that generates a traversal options structure  
        from the following items:  
        stopspec -   a find spec shorthand as input to cfg_findspec (see  
                     cfg_findspec for details)  
        clvl, mlvl - current/maximum tree level  
        cnt, mcnt - found items/maximum #items  
        dflag      - traverse val/values part of tree  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_tropts.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_tropts", *args, **kwargs)
