from spm.__wrapper__ import Runtime


def _seloverdim(*args, **kwargs):
  """seloverdim is a function.  
      data = seloverdim(data, seldim, sel, fb)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/seloverdim.m)
  """

  return Runtime.call("seloverdim", *args, **kwargs)
