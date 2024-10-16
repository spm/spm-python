from spm.__wrapper__ import Runtime


def _elec1020_follow(*args, **kwargs):
  """  ELEC1020_FOLLOW  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_follow.m)
  """

  return Runtime.call("elec1020_follow", *args, **kwargs)
