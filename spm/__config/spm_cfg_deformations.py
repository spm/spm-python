from spm.__wrapper__ import Runtime


def spm_cfg_deformations(*args, **kwargs):
  """  Configuration file for deformation jobs  
   _______________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_deformations.m)
  """

  return Runtime.call("spm_cfg_deformations", *args, **kwargs)
