from spm.__wrapper__ import Runtime


def test_spm_dctmtx(*args, **kwargs):
  """  Unit Tests for spm_dctmtx  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dctmtx.m)
  """

  return Runtime.call("test_spm_dctmtx", *args, **kwargs)
