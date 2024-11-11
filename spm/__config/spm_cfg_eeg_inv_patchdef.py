from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_patchdef(*args, **kwargs):
    """
      Configuration file for taking a number of previous inversion results  
        (maybe based on different data), smoothing and creating an approximate posterior  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_patchdef.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_eeg_inv_patchdef", *args, **kwargs)
