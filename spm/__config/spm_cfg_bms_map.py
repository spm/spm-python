from spm.__wrap__ import _Runtime


def spm_cfg_bms_map(*args, **kwargs):
  """  Configuration file for BMS interface  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_bms_map.m)
  """

  return _Runtime.call("spm_cfg_bms_map", *args, **kwargs)
