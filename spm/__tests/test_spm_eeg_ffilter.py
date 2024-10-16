from spm.__wrapper__ import Runtime


def test_spm_eeg_ffilter(*args, **kwargs):
  """  Unit Tests for spm_eeg_ffilter  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_eeg_ffilter.m)
  """

  return Runtime.call("test_spm_eeg_ffilter", *args, **kwargs)
