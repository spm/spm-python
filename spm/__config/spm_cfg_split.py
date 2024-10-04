from spm.__wrap__ import _Runtime


def spm_cfg_split(*args, **kwargs):
  """  SPM Configuration file for 4D to 3D volumes conversion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_split.m)
  """

  return _Runtime.call("spm_cfg_split", *args, **kwargs)
