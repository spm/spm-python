from spm.__wrap__ import _Runtime


def test_spm_opm_epoch_trigger(*args, **kwargs):
  """  Unit Tests for spm_eeg_average  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/tests/test_spm_opm_epoch_trigger.m)
  """

  return _Runtime.call("test_spm_opm_epoch_trigger", *args, **kwargs)
