from spm.__wrapper__ import Runtime


def tbx_cfg_render(*args, **kwargs):
  """  Configuration file for toolbox 'Rendering'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/SRender/tbx_cfg_render.m)
  """

  return Runtime.call("tbx_cfg_render", *args, **kwargs)
