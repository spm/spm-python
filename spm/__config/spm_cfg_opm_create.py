from spm._runtime import Runtime


def spm_cfg_opm_create(*args, **kwargs):
    r"""
      Configuration file for creating OPM objects  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_cfg_opm_create.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_opm_create", *args, **kwargs)
