from spm.__wrapper__ import Runtime


def spm_rewrite_job(*args, **kwargs):
    """
      Rewrite a batch job for SPM12  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_rewrite_job.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_rewrite_job", *args, **kwargs)
