from spm.__wrap__ import _Runtime


def test_spm_dcm_peb_bmc_fam(*args, **kwargs):
  """  Unit Tests for test_spm_dcm_peb_bmc_fam  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_peb_bmc_fam.m)
  """

  return _Runtime.call("test_spm_dcm_peb_bmc_fam", *args, **kwargs)
