from spm.__wrapper__ import Runtime


def spm_cfg_opm_synth_gradiometer(*args, **kwargs):
  """  Configuration file for performing synthetic gradiometery on OPM data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_opm_synth_gradiometer.m)
  """

  return Runtime.call("spm_cfg_opm_synth_gradiometer", *args, **kwargs)
