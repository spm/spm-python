from spm.__wrap__ import _Runtime


def _GALA_calculate_distance(*args, **kwargs):
  """GALA_calculate_distance is a function.  
      distance = GALA_calculate_distance(mesh)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_calculate_distance.m)
  """

  return _Runtime.call("GALA_calculate_distance", *args, **kwargs)
