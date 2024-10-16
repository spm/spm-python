from spm.__wrapper__ import Runtime


def test_spm_dcm_simulate(*args, **kwargs):
  """  Unit Tests for test_spm_dcm_simulate  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_simulate.m)
  """

  return Runtime.call("test_spm_dcm_simulate", *args, **kwargs)
