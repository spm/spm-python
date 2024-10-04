from spm.__wrap__ import _Runtime


def _cornerpoints(*args, **kwargs):
  """  CORNERPOINTS returns the eight corner points of an anatomical volume  
    in voxel and in head coordinates  
     
    Use as  
      [voxel, head] = cornerpoints(dim, transform)  
    which will return two 8x3 matrices.  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/cornerpoints.m)
  """

  return _Runtime.call("cornerpoints", *args, **kwargs)
