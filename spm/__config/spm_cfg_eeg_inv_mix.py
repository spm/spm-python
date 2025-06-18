from mpython import Runtime


def spm_cfg_eeg_inv_mix(*args, **kwargs):
    """
      Configuration file for merging (using a new inversion) a number of
        imaging source inversion reconstructions
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_mix.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_inv_mix", *args, **kwargs)
