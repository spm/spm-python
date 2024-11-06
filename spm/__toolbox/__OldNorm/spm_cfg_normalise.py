from spm.__wrapper__ import Runtime


def spm_cfg_normalise(*args, **kwargs):
    """
      SPM Configuration file for toolbox 'Old Normalise'  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_cfg_normalise.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_normalise", *args, **kwargs)
