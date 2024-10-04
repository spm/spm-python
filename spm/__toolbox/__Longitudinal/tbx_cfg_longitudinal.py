from spm.__wrap__ import _Runtime


def tbx_cfg_longitudinal(*args, **kwargs):
  """  MATLABBATCH Configuration file for toolbox 'Longitudinal'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Longitudinal/tbx_cfg_longitudinal.m)
  """

  return _Runtime.call("tbx_cfg_longitudinal", *args, **kwargs)
