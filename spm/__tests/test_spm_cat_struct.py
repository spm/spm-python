from spm.__wrap__ import _Runtime


def test_spm_cat_struct(*args, **kwargs):
  """  Unit Tests for spm_cat_struct  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_cat_struct.m)
  """

  return _Runtime.call("test_spm_cat_struct", *args, **kwargs)
