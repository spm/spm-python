from mpython import Runtime


def test_spm_dcm_peb_bmc_fam(*args, **kwargs):
    """
      Unit Tests for test_spm_dcm_peb_bmc_fam
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_dcm_peb_bmc_fam.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_dcm_peb_bmc_fam", *args, **kwargs)
