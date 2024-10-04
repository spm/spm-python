from spm.__wrap__ import _Runtime


def test_regress_spm_opm(*args, **kwargs):
  """  regresion test for OPM functions  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_regress_spm_opm.m)
  """

  return _Runtime.call("test_regress_spm_opm", *args, **kwargs)
