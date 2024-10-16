from spm.__wrapper__ import Runtime


def test_spm_bireduce(*args, **kwargs):
  """  Unit Tests for test_spm_bireduce  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_bireduce.m)
  """

  return Runtime.call("test_spm_bireduce", *args, **kwargs)
