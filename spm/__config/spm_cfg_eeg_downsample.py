from spm.__wrap__ import _Runtime


def spm_cfg_eeg_downsample(*args, **kwargs):
  """  Configuration file for M/EEG downsampling  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_downsample.m)
  """

  return _Runtime.call("spm_cfg_eeg_downsample", *args, **kwargs)
