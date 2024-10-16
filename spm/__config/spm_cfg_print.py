from spm.__wrapper__ import Runtime


def spm_cfg_print(*args, **kwargs):
  """  SPM Configuration file for 'Print figure'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_print.m)
  """

  return Runtime.call("spm_cfg_print", *args, **kwargs)
