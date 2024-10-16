from spm.__wrapper__ import Runtime


def spm_cfg_sendmail(*args, **kwargs):
  """  SPM Configuration file for sendmail  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_sendmail.m)
  """

  return Runtime.call("spm_cfg_sendmail", *args, **kwargs)
