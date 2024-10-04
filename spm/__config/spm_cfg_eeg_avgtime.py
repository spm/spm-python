from spm.__wrap__ import _Runtime


def spm_cfg_eeg_avgtime(*args, **kwargs):
  """  Configuration file for averaging over time  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_avgtime.m)
  """

  return _Runtime.call("spm_cfg_eeg_avgtime", *args, **kwargs)
