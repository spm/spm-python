from spm._runtime import Runtime


def spm_run_denoise(*args, **kwargs):
    r"""
      FORMAT out = spm_run_denoise(opt,cfg)  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_run_denoise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_run_denoise", *args, **kwargs)
