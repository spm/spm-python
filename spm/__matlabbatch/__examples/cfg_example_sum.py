from spm._runtime import Runtime


def cfg_example_sum(*args, **kwargs):
    """
      Example script that creates an cfg_exbranch to sum two numbers. The  
        inputs are entered as vector, the output is just a single  
        number. This function differs from cfg_example_add2 (except from names)  
        only in the specification of input1.num.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_sum.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_example_sum", *args, **kwargs)
