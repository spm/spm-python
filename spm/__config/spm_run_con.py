from spm._runtime import Runtime


def spm_run_con(*args, **kwargs):
    r"""
      SPM job execution function - Specify and estimate contrasts  
        Input:  
        job    - harvested job data structure (see matlabbatch help)  
        Output:  
        out    - struct containing contrast and SPM{.} images filename  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_run_con.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_con", *args, **kwargs)
