from spm.__wrapper__ import Runtime


def _elec1020_fraction(*args, **kwargs):
  """  ELEC1020_FRACTION  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_fraction.m)
  """

  return Runtime.call("elec1020_fraction", *args, **kwargs)
