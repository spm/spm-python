from mpython import Runtime


def spm_cfg_eeg_remove_bad_trials(*args, **kwargs):
    """
      configuration file for removing bad trials
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_remove_bad_trials.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_remove_bad_trials", *args, **kwargs)
