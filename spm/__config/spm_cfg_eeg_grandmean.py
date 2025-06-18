from mpython import Runtime


def spm_cfg_eeg_grandmean(*args, **kwargs):
    """
      Configuration file for averaging evoked responses
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_grandmean.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_grandmean", *args, **kwargs)
