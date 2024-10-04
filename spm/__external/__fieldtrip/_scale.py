from spm.__wrap__ import _Runtime


def _scale(*args, **kwargs):
  """  SCALE returns the homogenous coordinate transformation matrix  
    corresponding to a scaling along the x, y and z-axis  
      
    Use as  
      [H] = translate(S)  
    where  
      S   [sx, sy, sz] scaling along each of the axes  
      H   corresponding homogenous transformation matrix  
     
    See also TRANSLATE, ROTATE, RIGIDBODY, QUATERNION, HOMOGENOUS2TRADITIONAL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/scale.m)
  """

  return _Runtime.call("scale", *args, **kwargs)
