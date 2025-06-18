from mpython import Runtime


def spm_eeg_montage_ui(*args, **kwargs):
    """
      GUI for EEG montage (rereference EEG data to new reference channel(s))
        FORMAT montage = spm_eeg_montage_ui(montage)

        montage     - structure with fields:
          tra       - MxN matrix
          labelnew  - Mx1 cell-array - new labels
          labelorg  - Nx1 cell-array - original labels

        Output is empty if the GUI is closed.
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_montage_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_montage_ui", *args, **kwargs)
