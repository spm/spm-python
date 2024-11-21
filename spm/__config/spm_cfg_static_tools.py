from spm.__wrapper__ import Runtime


def spm_cfg_static_tools(*args, **kwargs):
    """
      Static listing of all batch configuration files in the SPM toolbox folder  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_static_tools.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_static_tools", *args, **kwargs)
