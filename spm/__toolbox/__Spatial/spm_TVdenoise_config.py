from spm.__wrapper__ import Runtime


def spm_TVdenoise_config(*args, **kwargs):
  """  SPM Configuration file for total variation denoising  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_TVdenoise_config.m)
  """

  return Runtime.call("spm_TVdenoise_config", *args, **kwargs)
