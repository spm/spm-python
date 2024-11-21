from spm.__wrapper__ import Runtime


def _rigidbody(*args, **kwargs):
    """
      RIGIDBODY creates the homogenous spatial transformation matrix  
        for a 6 parameter rigid-body transformation   
         
        Use as  
          [H] = rigidbody(f)  
         
        The transformation vector f should contain the   
          x-shift  
          y-shift  
          z-shift  
        followed by the  
          pitch (rotation around x-axis, in degrees)  
          roll  (rotation around y-axis, in degrees)  
          yaw   (rotation around z-axis, in degrees)  
         
        See also ROTATE, TRANSLATE, SCALE, QUATERNION, HOMOGENOUS2TRADITIONAL  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/rigidbody.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("rigidbody", *args, **kwargs)
