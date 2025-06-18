from mpython import Runtime


def spm_eeg_prep_ui(*args, **kwargs):
    """
      User interface for spm_eeg_prep function performing several tasks
        for preparation of converted MEEG data for further analysis
        FORMAT spm_eeg_prep_ui(callback)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_prep_ui.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_prep_ui", *args, **kwargs, nargout=0)
