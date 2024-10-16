from spm.__wrapper__ import Runtime


def spm_cfg_eeg_remove_bad_trials(*args, **kwargs):
  """  configuration file for removing bad trials  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_remove_bad_trials.m)
  """

  return Runtime.call("spm_cfg_eeg_remove_bad_trials", *args, **kwargs)
