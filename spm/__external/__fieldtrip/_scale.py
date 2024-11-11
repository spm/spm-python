from spm.__wrapper__ import Runtime


def _scale(*args, **kwargs):
    """
      SCALE returns the homogenous coordinate transformation matrix  
        corresponding to a scaling along the x, y and z-axis  
          
        Use as  
          [H] = translate(S)  
        where  
          S   [sx, sy, sz] scaling along each of the axes  
          H   corresponding homogenous transformation matrix  
         
        See also TRANSLATE, ROTATE, RIGIDBODY, QUATERNION, HOMOGENOUS2TRADITIONAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/scale.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("scale", *args, **kwargs)
