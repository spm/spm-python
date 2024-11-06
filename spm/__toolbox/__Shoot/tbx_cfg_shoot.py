from spm.__wrapper__ import Runtime


def tbx_cfg_shoot(*args, **kwargs):
    """
      MATLABBATCH Configuration file for toolbox 'Shoot Tools'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Shoot/tbx_cfg_shoot.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("tbx_cfg_shoot", *args, **kwargs)
