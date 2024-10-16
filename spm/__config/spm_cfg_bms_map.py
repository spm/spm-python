from spm.__wrapper__ import Runtime


def spm_cfg_bms_map(*args, **kwargs):
  """  Configuration file for BMS interface  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_bms_map.m)
  """

  return Runtime.call("spm_cfg_bms_map", *args, **kwargs)
