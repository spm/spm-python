from spm._runtime import Runtime


def spm_cfg_eeg_inv_post(*args, **kwargs):
    r"""
      Configuration file for taking a number of previous inversion results  
        (maybe based on different data), smoothing and creating an approximate posterior  
       __________________________________________________________________________  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/config/spm_cfg_eeg_inv_post.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_inv_post", *args, **kwargs)
