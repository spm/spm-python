from spm.__wrap__ import _Runtime


def test_spm_get_data(*args, **kwargs):
  """  Unit Tests for spm_get_data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_get_data.m)
  """

  return _Runtime.call("test_spm_get_data", *args, **kwargs)
