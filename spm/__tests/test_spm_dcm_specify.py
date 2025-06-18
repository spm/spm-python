from mpython import Runtime


def test_spm_dcm_specify(*args, **kwargs):
    """
      Unit Tests for spm_dcm_specify_ui
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_dcm_specify.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_dcm_specify", *args, **kwargs)
