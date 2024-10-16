from spm.__wrapper__ import Runtime


def spm_cfg_md(*args, **kwargs):
  """  SPM Configuration file for making directory function  
   _______________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_md.m)
  """

  return Runtime.call("spm_cfg_md", *args, **kwargs)
