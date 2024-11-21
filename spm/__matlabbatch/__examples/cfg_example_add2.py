from spm.__wrapper__ import Runtime


def cfg_example_add2(*args, **kwargs):
    """
      Example script that creates an cfg_exbranch to sum two numbers. The  
        inputs are entered as 2-vector, the output is just a single  
        number.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_add2.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_example_add2", *args, **kwargs)
