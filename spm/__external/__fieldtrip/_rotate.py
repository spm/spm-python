from spm.__wrapper__ import Runtime


def _rotate(*args, **kwargs):
    """
      ROTATE returns the homogenous coordinate transformation matrix  
        corresponding to a rotation around the x, y and z-axis. The direction of  
        the rotation is according to the right-hand rule.  
         
        Use as  
          [H] = rotate(R)  
        where  
          R   [rx, ry, rz] in degrees  
          H   corresponding homogenous transformation matrix  
         
        Note that the order in which the rotations are performs matters. The  
        rotation is first done around the z-axis, then the y-axis and finally the  
        x-axis.  
         
        See also TRANSLATE, SCALE, RIGIDBODY, QUATERNION, HOMOGENOUS2TRADITIONAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/rotate.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("rotate", *args, **kwargs)
