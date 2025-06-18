from mpython import Runtime


def spm_eeg_inv_checkforward(*args, **kwargs):
    """
      Check M/EEG forward model
        FORMAT spm_eeg_inv_checkforward(D, val, ind)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_checkforward.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_checkforward", *args, **kwargs, nargout=0)
