from spm.__wrap__ import _Runtime


def test_spm_ncTpdf(*args, **kwargs):
  """  Unit Tests for spm_ncTpdf  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_ncTpdf.m)
  """

  return _Runtime.call("test_spm_ncTpdf", *args, **kwargs)
