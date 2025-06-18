from mpython import Runtime


def spm_cfg_eeg_inv_priors(*args, **kwargs):
    """
      Configuration file to set up priors for M/EEG source reconstruction
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_priors.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_cfg_eeg_inv_priors", *args, **kwargs)
