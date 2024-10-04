from spm.__wrap__ import _Runtime


def spm_cfg_eeg_opmsetup(*args, **kwargs):
  """  Configuration file for M/EEG OPM set up  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_opmsetup.m)
  """

  return _Runtime.call("spm_cfg_eeg_opmsetup", *args, **kwargs)
