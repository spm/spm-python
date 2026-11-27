from spm._runtime import Runtime


def spm_lincom(*args, **kwargs):
    r"""
      Generate linear combinations of images  
        FORMAT spm_lincom(job)  
        job.images   - Images to use  
        job.weights  - Matrix of weights  
        job.basename - Part of filename for results  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Shoot/spm_lincom.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_lincom", *args, **kwargs)
