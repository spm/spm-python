from spm.__wrapper__ import Runtime


def spm_cfg_ppi(*args, **kwargs):
  """  SPM Configuration file for PPIs  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_ppi.m)
  """

  return Runtime.call("spm_cfg_ppi", *args, **kwargs)
