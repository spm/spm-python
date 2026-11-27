from spm._runtime import Runtime


def cfg_example_add2(*args, **kwargs):
    r"""
      Example script that creates an cfg_exbranch to sum two numbers. The  
        inputs are entered as 2-vector, the output is just a single  
        number.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/examples/cfg_example_add2.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_example_add2", *args, **kwargs)
