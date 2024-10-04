from spm.__wrap__ import _Runtime


def spm_cfg_parrec(*args, **kwargs):
  """  SPM Configuration file for Philips PAR/REC Import  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/spm_cfg_parrec.m)
  """

  return _Runtime.call("spm_cfg_parrec", *args, **kwargs)
