from spm.__wrapper__ import Runtime


def spm_cfg_render(*args, **kwargs):
    """
      SPM Configuration file for Render  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_render.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_render", *args, **kwargs)
