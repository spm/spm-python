from spm.__wrapper__ import Runtime


def spm_cfg_con(*args, **kwargs):
  """  SPM Configuration file for contrast specification  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_con.m)
  """

  return Runtime.call("spm_cfg_con", *args, **kwargs)
