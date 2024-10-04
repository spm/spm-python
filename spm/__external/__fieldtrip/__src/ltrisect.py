from spm.__wrap__ import _Runtime


def ltrisect(*args, **kwargs):
  """  LTRISECT intersects a line with a plane spanned by three vertices  
     
    Use as  
      [sect] = ltrisect(v1, v2, v3, l1, l2)  
    where v1, v2 and v3 are three vertices spanning the plane, and l1 and l2  
    are two points on the line  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/src/ltrisect.m)
  """

  return _Runtime.call("ltrisect", *args, **kwargs)
