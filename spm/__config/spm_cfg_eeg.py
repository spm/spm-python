from spm.__wrapper__ import Runtime


def spm_cfg_eeg(*args, **kwargs):
  """  SPM M/EEG Configuration file for MATLABBATCH  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg.m)
  """

  return Runtime.call("spm_cfg_eeg", *args, **kwargs)
