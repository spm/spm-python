from spm.__wrap__ import _Runtime


def _avgoverdim(*args, **kwargs):
  """avgoverdim is a function.  
      data = avgoverdim(data, avgdim, fb)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverdim.m)
  """

  return _Runtime.call("avgoverdim", *args, **kwargs)
