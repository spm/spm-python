from spm.__wrap__ import _Runtime


def spm_slice2vol_config(*args, **kwargs):
  """  Configuration file for toolbox 'Spatial Tools'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol_config.m)
  """

  return _Runtime.call("spm_slice2vol_config", *args, **kwargs)
