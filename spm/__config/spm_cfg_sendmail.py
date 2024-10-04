from spm.__wrap__ import _Runtime


def spm_cfg_sendmail(*args, **kwargs):
  """  SPM Configuration file for sendmail  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_sendmail.m)
  """

  return _Runtime.call("spm_cfg_sendmail", *args, **kwargs)
