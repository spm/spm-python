from spm._runtime import Runtime


def spm_cfg_eeg_inv_optimize(*args, **kwargs):
    """
      Configuration file to set up optimization routines for M/EEG source  
        inversion  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_optimize.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_inv_optimize", *args, **kwargs)
