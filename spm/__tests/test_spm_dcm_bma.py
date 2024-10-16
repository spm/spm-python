from spm.__wrapper__ import Runtime


def test_spm_dcm_bma(*args, **kwargs):
  """  Unit Tests for spm_dcm_bma  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_bma.m)
  """

  return Runtime.call("test_spm_dcm_bma", *args, **kwargs)
