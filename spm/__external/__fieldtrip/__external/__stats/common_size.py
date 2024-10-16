from spm.__wrapper__ import Runtime


def common_size(*args, **kwargs):
  """common_size is a function.  
      [errorcode, varargout] = common_size(varargin)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/common_size.m)
  """

  return Runtime.call("common_size", *args, **kwargs)
