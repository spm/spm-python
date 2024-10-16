from spm.__wrapper__ import Runtime


def spm_cfg_render(*args, **kwargs):
  """  SPM Configuration file for Render  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_render.m)
  """

  return Runtime.call("spm_cfg_render", *args, **kwargs)
