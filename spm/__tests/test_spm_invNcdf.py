from spm.__wrap__ import _Runtime


def test_spm_invNcdf(*args, **kwargs):
  """  Unit Tests for spm_invNcdf  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_invNcdf.m)
  """

  return _Runtime.call("test_spm_invNcdf", *args, **kwargs)
