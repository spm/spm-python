from spm.__wrapper__ import Runtime


def spm_cfg_realignunwarp(*args, **kwargs):
  """  SPM Configuration file for Realign & Unwarp  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_realignunwarp.m)
  """

  return Runtime.call("spm_cfg_realignunwarp", *args, **kwargs)
