from mpython import Runtime


def spm_cfg_eeg_bc(*args, **kwargs):
    """
      configuration file for baseline correction
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_bc.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_bc", *args, **kwargs)
