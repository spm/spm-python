from spm.__wrapper__ import Runtime


def test_spm_cat_struct(*args, **kwargs):
  """  Unit Tests for spm_cat_struct  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_cat_struct.m)
  """

  return Runtime.call("test_spm_cat_struct", *args, **kwargs)
