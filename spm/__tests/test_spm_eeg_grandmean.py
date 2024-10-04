from spm.__wrap__ import _Runtime


def test_spm_eeg_grandmean(*args, **kwargs):
  """  Unit Tests for spm_eeg_merge  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_eeg_grandmean.m)
  """

  return _Runtime.call("test_spm_eeg_grandmean", *args, **kwargs)
