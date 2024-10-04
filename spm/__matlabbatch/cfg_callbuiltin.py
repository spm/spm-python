from spm.__wrap__ import _Runtime


def cfg_callbuiltin(*args, **kwargs):
  """cfg_callbuiltin is a function.  
      varargout = cfg_callbuiltin(varargin)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/matlabbatch/cfg_callbuiltin.m)
  """

  return _Runtime.call("cfg_callbuiltin", *args, **kwargs)
