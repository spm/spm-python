from spm.__wrapper__ import Runtime


def spm_cfg_eeg_combineplanar(*args, **kwargs):
  """  configuration file for combineplanar  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_combineplanar.m)
  """

  return Runtime.call("spm_cfg_eeg_combineplanar", *args, **kwargs)
