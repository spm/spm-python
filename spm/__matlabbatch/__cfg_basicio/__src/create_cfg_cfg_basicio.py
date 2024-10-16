from spm.__wrapper__ import Runtime


def create_cfg_cfg_basicio(*args, **kwargs):
  """create_cfg_cfg_basicio is a function.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_basicio/src/create_cfg_cfg_basicio.m)
  """

  return Runtime.call("fileparts", *args, **kwargs)
