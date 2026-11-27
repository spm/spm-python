from spm._runtime import Runtime


def create_cfg_cfg_basicio(*args, **kwargs):
    r"""
    create_cfg_cfg_basicio is a function.  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/matlabbatch/cfg_basicio/src/create_cfg_cfg_basicio.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fileparts", *args, **kwargs)
