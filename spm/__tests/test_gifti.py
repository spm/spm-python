from spm.__wrap__ import _Runtime


def test_gifti(*args, **kwargs):
  """  Unit Tests for gifti  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_gifti.m)
  """

  return _Runtime.call("test_gifti", *args, **kwargs)
