from spm.__wrap__ import _Runtime


def spm_cfg_imcalc(*args, **kwargs):
  """  SPM Configuration file for ImCalc  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_imcalc.m)
  """

  return _Runtime.call("spm_cfg_imcalc", *args, **kwargs)
