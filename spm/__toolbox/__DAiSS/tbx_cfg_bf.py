from spm.__wrapper__ import Runtime


def tbx_cfg_bf(*args, **kwargs):
  """  Configuration file for toolbox 'Beamforming'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/tbx_cfg_bf.m)
  """

  return Runtime.call("tbx_cfg_bf", *args, **kwargs)
