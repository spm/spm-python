from spm.__wrap__ import _Runtime


def _vline(*args, **kwargs):
  """  VLINE plot a vertical line in the current graph  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/vline.m)
  """

  return _Runtime.call("vline", *args, **kwargs, nargout=0)
