from spm.__wrapper__ import Runtime


def _selfromraw(*args, **kwargs):
  """  FIXME this function is not documented  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/selfromraw.m)
  """

  return Runtime.call("selfromraw", *args, **kwargs)
