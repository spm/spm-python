from spm.__wrapper__ import Runtime


def spm_mb_init(*args, **kwargs):
  """  Initialisation of Multi-Brain data structures  
    FORMAT [dat,sett] = spm_mb_init(cfg)  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/MB/spm_mb_init.m)
  """

  return Runtime.call("spm_mb_init", *args, **kwargs)
