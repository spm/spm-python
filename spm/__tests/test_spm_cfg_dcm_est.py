from mpython import Runtime


def test_spm_cfg_dcm_est(*args, **kwargs):
    """
      Unit Tests for test_spm_cfg_dcm_est (DCM model estimation batch)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_cfg_dcm_est.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_cfg_dcm_est", *args, **kwargs)
