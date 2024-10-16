from spm.__wrapper__ import Runtime


def spm_cfg_static_tools(*args, **kwargs):
  """  Static listing of all batch configuration files in the SPM toolbox folder  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_static_tools.m)
  """

  return Runtime.call("spm_cfg_static_tools", *args, **kwargs)
