from mpython import Runtime


def spm_eeg_inv_forward(*args, **kwargs):
    """
      Compute M/EEG leadfield
        FORMAT D = spm_eeg_inv_forward(D,val)

        D                - input struct
        (optional) fields of S:
        D                - filename of EEG/MEG mat-file

        Output:
        D                - EEG/MEG struct with filenames of Gain matrices)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_forward.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_forward", *args, **kwargs)
