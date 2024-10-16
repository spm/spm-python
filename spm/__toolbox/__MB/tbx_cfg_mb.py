from spm.__wrapper__ import Runtime


def tbx_cfg_mb(*args, **kwargs):
  """  MATLABBATCH Configuration file for toolbox 'Multi-Brain'  
   _____________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/tbx_cfg_mb.m)
  """

  return Runtime.call("tbx_cfg_mb", *args, **kwargs)
