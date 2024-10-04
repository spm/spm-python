from spm.__wrap__ import _Runtime


def spm_TVdenoise_config(*args, **kwargs):
  """  SPM Configuration file for total variation denoising  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_TVdenoise_config.m)
  """

  return _Runtime.call("spm_TVdenoise_config", *args, **kwargs)
