from spm.__wrapper__ import Runtime


def test_spm_dcm_fit(*args, **kwargs):
  """  Unit Tests for spm_dcm_fit  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_fit.m)
  """

  return Runtime.call("test_spm_dcm_fit", *args, **kwargs)
