from spm.__wrapper__ import Runtime


def spm_scope_config(*args, **kwargs):
    """
      SPM Configuration file for SCOPE distortion correction  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_scope_config.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_scope_config", *args, **kwargs)
