from spm._runtime import Runtime


def spm_pairwise(*args, **kwargs):
    r"""
      Longitudinal registration of image pairs  
        FORMAT out = spm_pairwise(job)  
        See tbx_cfg_longitudinal.m for a description of the various fields.   
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Longitudinal/spm_pairwise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_pairwise", *args, **kwargs)
