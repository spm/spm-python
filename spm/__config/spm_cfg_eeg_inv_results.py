from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_results(*args, **kwargs):
  """  Configuration file for exporting results of source reconstruction  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_results.m)
  """

  return Runtime.call("spm_cfg_eeg_inv_results", *args, **kwargs)
