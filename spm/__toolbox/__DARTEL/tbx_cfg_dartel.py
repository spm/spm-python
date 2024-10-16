from spm.__wrapper__ import Runtime


def tbx_cfg_dartel(*args, **kwargs):
  """  Configuration file for toolbox 'Dartel Tools'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DARTEL/tbx_cfg_dartel.m)
  """

  return Runtime.call("tbx_cfg_dartel", *args, **kwargs)
