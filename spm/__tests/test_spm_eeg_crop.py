from spm.__wrap__ import _Runtime


def test_spm_eeg_crop(*args, **kwargs):
  """  Unit Tests for spm_eeg_crop  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_eeg_crop.m)
  """

  return _Runtime.call("test_spm_eeg_crop", *args, **kwargs)
