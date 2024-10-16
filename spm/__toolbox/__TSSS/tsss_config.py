from spm.__wrapper__ import Runtime


def tsss_config(*args, **kwargs):
  """  Configuration file for TSSS clean-up for Neuromag data  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/TSSS/tsss_config.m)
  """

  return Runtime.call("tsss_config", *args, **kwargs)
