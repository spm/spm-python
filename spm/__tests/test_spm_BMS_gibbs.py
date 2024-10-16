from spm.__wrapper__ import Runtime


def test_spm_BMS_gibbs(*args, **kwargs):
  """  Unit Tests for spm_BMS_gibbs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_BMS_gibbs.m)
  """

  return Runtime.call("test_spm_BMS_gibbs", *args, **kwargs)
