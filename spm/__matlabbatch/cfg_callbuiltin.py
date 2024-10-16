from spm.__wrapper__ import Runtime


def cfg_callbuiltin(*args, **kwargs):
  """cfg_callbuiltin is a function.  
      varargout = cfg_callbuiltin(varargin)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_callbuiltin.m)
  """

  return Runtime.call("cfg_callbuiltin", *args, **kwargs)
