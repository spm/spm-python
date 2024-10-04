from spm.__wrap__ import _Runtime


def spm_cfg_exp_frames(*args, **kwargs):
  """  SPM Configuration file for Expand Image Frames  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_exp_frames.m)
  """

  return _Runtime.call("spm_cfg_exp_frames", *args, **kwargs)
