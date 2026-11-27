from spm._runtime import Runtime


def spm_dartel_norm(*args, **kwargs):
    r"""
      Warp individuals to match template  
        FORMAT spm_dartel_norm(job)  
        job.flowfields - Flow-fields  
        job.images     - Image to warp  
        job.interp     - Interpolation method  
        job.K          - 2^K timesteps are used  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/DARTEL/spm_dartel_norm.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_dartel_norm", *args, **kwargs)
