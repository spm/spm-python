from spm._runtime import Runtime


def cfg_example_run_cumsum1(*args, **kwargs):
    r"""
      Example function that returns the cumulative sum of an vector given in  
        job.a in out. The output is referenced as out(:), this is defined in  
        cfg_example_vout_cumsum1.  
         
        This code is part of a batch job configuration system for MATLAB. See   
             help matlabbatch  
        for a general overview.  
       _______________________________________________________________________  
        Copyright (C) 2007 Freiburg Brain Imaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/examples/cfg_example_run_cumsum1.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cfg_example_run_cumsum1", *args, **kwargs)
