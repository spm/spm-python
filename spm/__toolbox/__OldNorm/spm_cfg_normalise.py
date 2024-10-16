from spm.__wrapper__ import Runtime


def spm_cfg_normalise(*args, **kwargs):
  """  SPM Configuration file for toolbox 'Old Normalise'  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/OldNorm/spm_cfg_normalise.m)
  """

  return Runtime.call("spm_cfg_normalise", *args, **kwargs)
