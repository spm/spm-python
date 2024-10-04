from spm.__wrap__ import _Runtime


def _seloverdim(*args, **kwargs):
  """seloverdim is a function.  
      data = seloverdim(data, seldim, sel, fb)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/seloverdim.m)
  """

  return _Runtime.call("seloverdim", *args, **kwargs)
