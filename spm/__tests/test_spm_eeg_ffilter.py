from mpython import Runtime


def test_spm_eeg_ffilter(*args, **kwargs):
    """
      Unit Tests for spm_eeg_ffilter
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_eeg_ffilter.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_eeg_ffilter", *args, **kwargs)
