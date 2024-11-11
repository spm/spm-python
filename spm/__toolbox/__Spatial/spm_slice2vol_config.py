from spm.__wrapper__ import Runtime


def spm_slice2vol_config(*args, **kwargs):
    """
      Configuration file for toolbox 'Spatial Tools'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol_config.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_slice2vol_config", *args, **kwargs)
