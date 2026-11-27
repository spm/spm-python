from spm._runtime import Runtime


def spm_slice2vol_config(*args, **kwargs):
    r"""
      Configuration file for toolbox 'Spatial Tools'  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/Spatial/spm_slice2vol_config.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_slice2vol_config", *args, **kwargs)
