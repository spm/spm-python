from spm._runtime import Runtime


def tbx_cfg_bsd(*args, **kwargs):
    r"""
      Configuration file for toolbox 'Bayesian Spectral Decomposition'  
       _______________________________________________________________________  
        Copyright (C) 2024-2025 Wellcome Trust Centre for Neuroimaging  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/toolbox/BSD/tbx_cfg_bsd.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tbx_cfg_bsd", *args, **kwargs)
