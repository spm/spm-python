from spm._runtime import Runtime


def spm_cfg_eeg_inv_coregshift(*args, **kwargs):
    r"""
      Configuration file for specifying the head model for source  
        reconstruction. This is to add deterministic or random displacements to  
        simulate coregistration error.  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_cfg_eeg_inv_coregshift.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_inv_coregshift", *args, **kwargs)
