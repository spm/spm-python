from spm.__wrapper__ import Runtime


def spm_cfg_realign(*args, **kwargs):
  """  SPM Configuration file for Realign  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_realign.m)
  """

  return Runtime.call("spm_cfg_realign", *args, **kwargs)
