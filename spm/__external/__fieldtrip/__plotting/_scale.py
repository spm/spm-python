from spm._runtime import Runtime


def _scale(*args, **kwargs):
    r"""
      SCALE returns the homogenous coordinate transformation matrix  
        corresponding to a scaling along the x, y and z-axis  
          
        Use as  
          [H] = translate(S)  
        where  
          S   [sx, sy, sz] scaling along each of the axes  
          H   corresponding homogenous transformation matrix  
         
        See also TRANSLATE, ROTATE, RIGIDBODY, QUATERNION, HOMOGENOUS2TRADITIONAL  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/scale.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("scale", *args, **kwargs)
