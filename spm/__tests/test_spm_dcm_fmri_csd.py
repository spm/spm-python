from mpython import Runtime


def test_spm_dcm_fmri_csd(*args, **kwargs):
    """
      Unit Tests for spm_dcm_fmri_csd
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_dcm_fmri_csd.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_dcm_fmri_csd", *args, **kwargs)
