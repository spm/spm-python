from spm._runtime import Runtime


def test_spm_dcm_peb_to_gcm(*args, **kwargs):
    """
      Unit Tests for spm_dcm_peb_to_gcm  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_dcm_peb_to_gcm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_dcm_peb_to_gcm", *args, **kwargs)
