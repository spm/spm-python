from spm.__wrap__ import _Runtime


def test_spm(*args, **kwargs):
  """  Unit Tests for spm  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm.m)
  """

  return _Runtime.call("test_spm", *args, **kwargs)
