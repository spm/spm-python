from spm.__wrap__ import _Runtime


def spm_cfg_eeg_firstlevel(*args, **kwargs):
  """  SPM Configuration file for M/EEG convolution modelling  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_firstlevel.m)
  """

  return _Runtime.call("spm_cfg_eeg_firstlevel", *args, **kwargs)
