from mpython import Runtime


def spm_eeg_inv_check(*args, **kwargs):
    """
      Checks that the EEG/MEG .mat file structure is loaded properly and that
        the particular inversion of interest has been specified

        FORMAT [D,val] = spm_eeg_inv_check(D,[val])
        Input:
        S              - data structure or its filename
        val            - model of interest (usually 1)
        Output:
        D              - data structure
        val            - model of interest D.val
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/spm_eeg_inv_check.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("spm_eeg_inv_check", *args, **kwargs)
