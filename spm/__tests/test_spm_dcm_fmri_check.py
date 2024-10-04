from spm.__wrap__ import _Runtime


def test_spm_dcm_fmri_check(*args, **kwargs):
  """  Unit Tests for spm_dcm_fmri_check  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_fmri_check.m)
  """

  return _Runtime.call("test_spm_dcm_fmri_check", *args, **kwargs)
