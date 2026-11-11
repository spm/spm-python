from spm._runtime import Runtime


def spm_scope_config(*args, **kwargs):
    r"""
      SPM Configuration file for SCOPE distortion correction  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_scope_config.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_scope_config", *args, **kwargs)
