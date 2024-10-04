from spm.__wrap__ import _Runtime


def test_spm_dcm_specify(*args, **kwargs):
  """  Unit Tests for spm_dcm_specify_ui  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_dcm_specify.m)
  """

  return _Runtime.call("test_spm_dcm_specify", *args, **kwargs)
