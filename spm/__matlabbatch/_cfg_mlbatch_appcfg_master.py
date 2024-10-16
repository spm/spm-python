from spm.__wrapper__ import Runtime


def _cfg_mlbatch_appcfg_master(*args, **kwargs):
  """cfg_mlbatch_appcfg_master is a function.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/private/cfg_mlbatch_appcfg_master.m)
  """

  return Runtime.call("cfg_mlbatch_appcfg_master", *args, **kwargs, nargout=0)
