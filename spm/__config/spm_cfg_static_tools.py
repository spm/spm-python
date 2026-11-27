from spm._runtime import Runtime


def spm_cfg_static_tools(*args, **kwargs):
    r"""
      Static listing of all batch configuration files in the SPM toolbox folder  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_cfg_static_tools.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_static_tools", *args, **kwargs)
