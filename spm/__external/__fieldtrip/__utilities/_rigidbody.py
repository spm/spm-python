from spm._runtime import Runtime


def _rigidbody(*args, **kwargs):
    r"""
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
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/rigidbody.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("rigidbody", *args, **kwargs)
