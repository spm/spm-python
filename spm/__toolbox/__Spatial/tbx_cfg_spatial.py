from spm.__wrapper__ import Runtime


def tbx_cfg_spatial(*args, **kwargs):
  """  Configuration file for toolbox 'Spatial Tools'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/tbx_cfg_spatial.m)
  """

  return Runtime.call("tbx_cfg_spatial", *args, **kwargs)
