from mpython import Runtime


def spm_eeg_dipoles_ui(*args, **kwargs):
    """
      Get dipole locations and orientations from the user
        FORMAT dipoles = spm_eeg_dipoles_ui
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_dipoles_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_dipoles_ui", *args, **kwargs)
