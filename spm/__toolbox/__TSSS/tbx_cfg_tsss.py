from spm.__wrap__ import _Runtime


def tbx_cfg_tsss(*args, **kwargs):
  """  Configuration file for toolbox 'TSSS'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/TSSS/tbx_cfg_tsss.m)
  """

  return _Runtime.call("tbx_cfg_tsss", *args, **kwargs)
