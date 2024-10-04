from spm.__wrap__ import _Runtime


def _avgoverlabel(*args, **kwargs):
  """avgoverlabel is a function.  
      str = avgoverlabel(label)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverlabel.m)
  """

  return _Runtime.call("avgoverlabel", *args, **kwargs)
