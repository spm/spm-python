from spm.__wrapper__ import Runtime


def _hline(*args, **kwargs):
  """  HLINE plot a horizontal line in the current graph  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/hline.m)
  """

  return Runtime.call("hline", *args, **kwargs, nargout=0)
