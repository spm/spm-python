from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_headmodel(*args, **kwargs):
    """
      Configuration file for specifying the head model for source reconstruction  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_headmodel.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("spm_cfg_eeg_inv_headmodel", *args, **kwargs)
