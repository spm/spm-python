from mpython import Runtime


def test_spm_cfg_dcm_fmri(*args, **kwargs):
    """
      Unit Tests for spm_cfg_dcm_fmri (DCM fMRI spec batch)
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_cfg_dcm_fmri.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_cfg_dcm_fmri", *args, **kwargs)
