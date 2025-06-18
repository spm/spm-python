from mpython import Runtime


def spm_eeg_convert_ui(*args, **kwargs):
    """
      User interface for M/EEG data conversion facility
        FORMAT spm_eeg_convert_ui

        See spm_eeg_convert for details.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_convert_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_convert_ui", *args, **kwargs, nargout=0)
