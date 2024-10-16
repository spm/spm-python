from spm.__wrapper__ import Runtime


def test_spm_eeg_load(*args, **kwargs):
  """  Unit Tests for spm_eeg_load  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_eeg_load.m)
  """

  return Runtime.call("test_spm_eeg_load", *args, **kwargs)
