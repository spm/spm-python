from spm.__wrapper__ import Runtime


def spm_cfg_eeg_firstlevel(*args, **kwargs):
  """  SPM Configuration file for M/EEG convolution modelling  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_firstlevel.m)
  """

  return Runtime.call("spm_cfg_eeg_firstlevel", *args, **kwargs)
