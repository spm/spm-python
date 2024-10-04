from spm.__wrap__ import _Runtime


def spm_cfg_eeg_remove_bad_trials(*args, **kwargs):
  """  configuration file for removing bad trials  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_remove_bad_trials.m)
  """

  return _Runtime.call("spm_cfg_eeg_remove_bad_trials", *args, **kwargs)
