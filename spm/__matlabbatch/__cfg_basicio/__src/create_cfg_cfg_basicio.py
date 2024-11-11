from spm.__wrapper__ import Runtime


def create_cfg_cfg_basicio(*args, **kwargs):
    """
    create_cfg_cfg_basicio is a function.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/src/create_cfg_cfg_basicio.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("fileparts", *args, **kwargs)
