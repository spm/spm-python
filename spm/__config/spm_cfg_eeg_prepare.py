from spm._runtime import Runtime


def spm_cfg_eeg_prepare(*args, **kwargs):
    """
      Configuration file for the prepare tool  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_prepare.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_prepare", *args, **kwargs)
