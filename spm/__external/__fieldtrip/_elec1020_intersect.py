from spm.__wrapper__ import Runtime


def _elec1020_intersect(*args, **kwargs):
  """  ELEC1020_INTERSECT determines the intersection of a mesh with a plane  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_intersect.m)
  """

  return Runtime.call("elec1020_intersect", *args, **kwargs)
