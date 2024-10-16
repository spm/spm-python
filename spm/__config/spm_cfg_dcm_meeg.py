from spm.__wrapper__ import Runtime


def spm_cfg_dcm_meeg(*args, **kwargs):
  """  Invert multiple DCMs specified in GUI.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_dcm_meeg.m)
  """

  return Runtime.call("spm_cfg_dcm_meeg", *args, **kwargs)
