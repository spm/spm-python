from spm.__wrap__ import _Runtime


def test_spm_dcm_fmri_csd(*args, **kwargs):
  """  Unit Tests for spm_dcm_fmri_csd  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_fmri_csd.m)
  """

  return _Runtime.call("test_spm_dcm_fmri_csd", *args, **kwargs)
