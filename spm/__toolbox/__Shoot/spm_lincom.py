from spm.__wrapper__ import Runtime


def spm_lincom(*args, **kwargs):
    """
      Generate linear combinations of images  
        FORMAT spm_lincom(job)  
        job.images   - Images to use  
        job.weights  - Matrix of weights  
        job.basename - Part of filename for results  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/spm_lincom.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_lincom", *args, **kwargs)
