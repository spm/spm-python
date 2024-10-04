from spm.__wrap__ import _Runtime


def spm_cfg_eeg_inv_sensorshift(*args, **kwargs):
  """  Configuration file for tinkering with channel loations  
    This is to add deterministic or random displacements to simulate  
    coregistration error.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_inv_sensorshift.m)
  """

  return _Runtime.call("spm_cfg_eeg_inv_sensorshift", *args, **kwargs)
