from spm.__wrapper__ import Runtime


def test_spm_cfg_dcm_est(*args, **kwargs):
  """  Unit Tests for test_spm_cfg_dcm_est (DCM model estimation batch)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_cfg_dcm_est.m)
  """

  return Runtime.call("test_spm_cfg_dcm_est", *args, **kwargs)
