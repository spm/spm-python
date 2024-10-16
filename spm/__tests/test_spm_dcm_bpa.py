from spm.__wrapper__ import Runtime


def test_spm_dcm_bpa(*args, **kwargs):
  """  Unit Tests for spm_cfg_dcm_peb (PEB batch)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_bpa.m)
  """

  return Runtime.call("test_spm_dcm_bpa", *args, **kwargs)
