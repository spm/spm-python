from mpython import Runtime


def spm_cfg_eeg_merge(*args, **kwargs):
    """
      Configuration file for merging M/EEG files
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_merge.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_merge", *args, **kwargs)
