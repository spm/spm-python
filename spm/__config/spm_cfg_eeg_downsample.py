from mpython import Runtime


def spm_cfg_eeg_downsample(*args, **kwargs):
    """
      Configuration file for M/EEG downsampling
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_downsample.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_downsample", *args, **kwargs)
