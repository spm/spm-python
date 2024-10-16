from spm.__wrapper__ import Runtime


def test_spm_ncFcdf(*args, **kwargs):
  """  Unit Tests for spm_ncFcdf  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_ncFcdf.m)
  """

  return Runtime.call("test_spm_ncFcdf", *args, **kwargs)
