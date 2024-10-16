from spm.__wrapper__ import Runtime


def _avgoverlabel(*args, **kwargs):
  """avgoverlabel is a function.  
      str = avgoverlabel(label)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverlabel.m)
  """

  return Runtime.call("avgoverlabel", *args, **kwargs)
