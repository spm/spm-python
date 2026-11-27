from spm._runtime import Runtime


def spm_cfg_eeg_combineplanar(*args, **kwargs):
    r"""
      configuration file for combineplanar  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_cfg_eeg_combineplanar.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_combineplanar", *args, **kwargs)
