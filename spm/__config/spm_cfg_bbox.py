from spm.__wrapper__ import Runtime


def spm_cfg_bbox(*args, **kwargs):
  """  SPM Configuration file for Get Bounding Box  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_bbox.m)
  """

  return Runtime.call("spm_cfg_bbox", *args, **kwargs)
