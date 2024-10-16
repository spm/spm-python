from spm.__wrapper__ import Runtime


def spm_run_dcm_bms_vis(*args, **kwargs):
  """  Review BMS results  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_run_dcm_bms_vis.m)
  """

  return Runtime.call("spm_run_dcm_bms_vis", *args, **kwargs)
