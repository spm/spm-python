from spm.__wrapper__ import Runtime


def spm_cfg_opm_epoch_trigger(*args, **kwargs):
  """  Configuration file for epoching OPM data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_opm_epoch_trigger.m)
  """

  return Runtime.call("spm_cfg_opm_epoch_trigger", *args, **kwargs)
