from spm._runtime import Runtime


def spm_TVdenoise_config(*args, **kwargs):
    r"""
      SPM Configuration file for total variation denoising  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_TVdenoise_config.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_TVdenoise_config", *args, **kwargs)
