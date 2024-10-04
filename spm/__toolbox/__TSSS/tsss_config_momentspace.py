from spm.__wrap__ import _Runtime


def tsss_config_momentspace(*args, **kwargs):
  """  Configuration file for TSSS space conversion  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/TSSS/tsss_config_momentspace.m)
  """

  return _Runtime.call("tsss_config_momentspace", *args, **kwargs)
