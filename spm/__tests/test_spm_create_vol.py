from spm.__wrap__ import _Runtime


def test_spm_create_vol(*args, **kwargs):
  """  Unit Tests for spm_create_vol  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_create_vol.m)
  """

  return _Runtime.call("test_spm_create_vol", *args, **kwargs)
