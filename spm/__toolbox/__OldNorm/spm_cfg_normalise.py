from spm._runtime import Runtime


def spm_cfg_normalise(*args, **kwargs):
    r"""
      SPM Configuration file for toolbox 'Old Normalise'  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/OldNorm/spm_cfg_normalise.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_normalise", *args, **kwargs)
