from spm.__wrap__ import _Runtime


def _leadfield_interpolate(*args, **kwargs):
  """  LEADFIELD_INTERPOLATE interpolates the leadfield for a source at  
    an arbitrary location given the pre-computed leadfields on a regular  
    grid.  
     
    Use as  
      lf = leadfield_interpolate(pos, vol)  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/leadfield_interpolate.m)
  """

  return _Runtime.call("leadfield_interpolate", *args, **kwargs)
