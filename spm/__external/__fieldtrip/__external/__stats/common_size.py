from spm.__wrap__ import _Runtime


def common_size(*args, **kwargs):
  """common_size is a function.  
      [errorcode, varargout] = common_size(varargin)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/common_size.m)
  """

  return _Runtime.call("common_size", *args, **kwargs)
