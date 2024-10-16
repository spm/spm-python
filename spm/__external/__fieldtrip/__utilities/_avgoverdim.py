from spm.__wrapper__ import Runtime


def _avgoverdim(*args, **kwargs):
  """avgoverdim is a function.  
      data = avgoverdim(data, avgdim, fb)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverdim.m)
  """

  return Runtime.call("avgoverdim", *args, **kwargs)
