from spm._runtime import Runtime


def spm_run_reorient(*args, **kwargs):
    r"""
      SPM job execution function  
        takes a harvested job data structure and call SPM functions to perform  
        computations on the data.  
        Input:  
        job    - harvested job data structure (see matlabbatch help)  
        Output:  
        out    - computation results, usually a struct variable.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_run_reorient.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_reorient", *args, **kwargs)
