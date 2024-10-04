from spm.__wrap__ import _Runtime


def test_spm_dcm_peb_review(*args, **kwargs):
  """  Unit Tests for test_spm_dcm_peb_review. Simply ensures that the GUI  
    doesn't crash with different inputs.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_peb_review.m)
  """

  return _Runtime.call("test_spm_dcm_peb_review", *args, **kwargs)
