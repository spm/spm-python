from spm.__wrapper__ import Runtime


def test_spm_openmp(*args, **kwargs):
  """  Unit Tests for OpenMP  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_openmp.m)
  """

  return Runtime.call("test_spm_openmp", *args, **kwargs)
