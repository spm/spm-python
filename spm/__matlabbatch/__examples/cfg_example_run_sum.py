from spm.__wrapper__ import Runtime


def cfg_example_run_sum(*args, **kwargs):
    """
      Example function that returns the sum of an vector given in job.a in out.  
        The output is referenced as out(1), this is defined in  
        cfg_example_vout_sum.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/examples/cfg_example_run_sum.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("cfg_example_run_sum", *args, **kwargs)
