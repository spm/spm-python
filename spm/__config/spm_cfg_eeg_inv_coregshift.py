from spm.__wrapper__ import Runtime


def spm_cfg_eeg_inv_coregshift(*args, **kwargs):
  """  Configuration file for specifying the head model for source  
    reconstruction. This is to add deterministic or random displacements to  
    simulate coregistration error.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_coregshift.m)
  """

  return Runtime.call("spm_cfg_eeg_inv_coregshift", *args, **kwargs)
