from spm.__wrapper__ import Runtime


def spm_run_denoise(*args, **kwargs):
  """  FORMAT out = spm_run_denoise(opt,cfg)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/Spatial/spm_run_denoise.m)
  """

  return Runtime.call("spm_run_denoise", *args, **kwargs)
