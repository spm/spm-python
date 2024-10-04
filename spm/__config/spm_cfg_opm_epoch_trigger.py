from spm.__wrap__ import _Runtime


def spm_cfg_opm_epoch_trigger(*args, **kwargs):
  """  Configuration file for epoching OPM data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_opm_epoch_trigger.m)
  """

  return _Runtime.call("spm_cfg_opm_epoch_trigger", *args, **kwargs)
