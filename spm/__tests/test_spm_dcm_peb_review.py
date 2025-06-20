from spm._runtime import Runtime


def test_spm_dcm_peb_review(*args, **kwargs):
    """
      Unit Tests for test_spm_dcm_peb_review. Simply ensures that the GUI  
        doesn't crash with different inputs.  
       __________________________________________________________________________  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/tests/test_spm_dcm_peb_review.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("test_spm_dcm_peb_review", *args, **kwargs)
