from spm.__wrap__ import _Runtime


def test_spm_opm_rpsd(*args, **kwargs):
  """  Unit Tests for spm_opm_rpsd  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_opm_rpsd.m)
  """

  return _Runtime.call("test_spm_opm_rpsd", *args, **kwargs)
