from spm.__wrap__ import _Runtime


def spm_cfg_deformations(*args, **kwargs):
  """  Configuration file for deformation jobs  
   _______________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_deformations.m)
  """

  return _Runtime.call("spm_cfg_deformations", *args, **kwargs)
