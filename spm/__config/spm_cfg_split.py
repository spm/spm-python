from spm._runtime import Runtime


def spm_cfg_split(*args, **kwargs):
    r"""
      SPM Configuration file for 4D to 3D volumes conversion  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_cfg_split.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_split", *args, **kwargs)
