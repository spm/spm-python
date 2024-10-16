from spm.__wrapper__ import Runtime


def test_regress_fmri_group(*args, **kwargs):
  """  Regression tests for second-level SPM for fMRI  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_regress_fmri_group.m)
  """

  return Runtime.call("test_regress_fmri_group", *args, **kwargs)
