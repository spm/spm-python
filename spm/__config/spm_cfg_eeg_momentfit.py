from spm.__wrap__ import _Runtime


def spm_cfg_eeg_momentfit(*args, **kwargs):
  """  Configuration file for imaging source inversion reconstruction.  
    This version to supply position and orientation parameters idea is to  
    estimate dipole moments given priors and return a model evidence for  
    these priors.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_eeg_momentfit.m)
  """

  return _Runtime.call("spm_cfg_eeg_momentfit", *args, **kwargs)
