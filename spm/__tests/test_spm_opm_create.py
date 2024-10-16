from spm.__wrapper__ import Runtime


def test_spm_opm_create(*args, **kwargs):
  """  Unit Tests for spm_opm_hfc  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_opm_create.m)
  """

  return Runtime.call("test_spm_opm_create", *args, **kwargs)
