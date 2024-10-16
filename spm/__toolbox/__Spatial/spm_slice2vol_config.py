from spm.__wrapper__ import Runtime


def spm_slice2vol_config(*args, **kwargs):
  """  Configuration file for toolbox 'Spatial Tools'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_slice2vol_config.m)
  """

  return Runtime.call("spm_slice2vol_config", *args, **kwargs)
