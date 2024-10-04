from spm.__wrap__ import _Runtime


def tbx_cfg_shoot(*args, **kwargs):
  """  MATLABBATCH Configuration file for toolbox 'Shoot Tools'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Shoot/tbx_cfg_shoot.m)
  """

  return _Runtime.call("tbx_cfg_shoot", *args, **kwargs)
