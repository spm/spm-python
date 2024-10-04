from spm.__wrap__ import _Runtime


def cfg_mlbatch_appcfg(*args, **kwargs):
  """  Add SPM to the application list of MATLABBATCH  
    This file must be on MATLAB search path for cfg_util to detect it.  
   __________________________________________________________________________  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/config/cfg_mlbatch_appcfg.m)
  """

  return _Runtime.call("cfg_mlbatch_appcfg", *args, **kwargs)
