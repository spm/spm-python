from spm._runtime import Runtime


def spm_run_factorial_design(*args, **kwargs):
    r"""
      SPM job execution function - factorial design specification  
        Input:  
        job    - harvested job data structure (see matlabbatch help)  
        Output:  
        out    - struct variable containing the path of the saved SPM.mat  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_run_factorial_design.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_factorial_design", *args, **kwargs)
