from spm.__wrap__ import _Runtime


def _translate(*args, **kwargs):
  """  TRANSLATE returns the homogenous coordinate transformation matrix  
    corresponding to a translation along the x, y and z-axis  
     
    Use as  
      [H] = translate(T)  
    where  
      T   [tx, ty, tz] translation along each of the axes  
      H   corresponding homogenous transformation matrix  
     
    See also ROTATE, SCALE, RIGIDBODY, QUATERNION, HOMOGENOUS2TRADITIONAL  
  

  [Link to the Matlab implementation.](https://github.com/spm/spm/blob/main/external/fieldtrip/private/translate.m)
  """

  return _Runtime.call("translate", *args, **kwargs)
