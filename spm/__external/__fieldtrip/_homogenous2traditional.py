from spm.__wrapper__ import Runtime


def _homogenous2traditional(*args, **kwargs):
    """
      HOMOGENOUS2TRADITIONAL estimates the traditional translation, rotation  
        and scaling parameters from a homogenous transformation matrix. It will  
        give an error if the homogenous matrix also describes a perspective  
        transformation.  
         
        Use as  
          f = homogenous2traditional(H)  
        where H is a 4x4 homogenous transformation matrix and f is a vector with  
        nine elements describing  
          x-shift  
       	  y-shift  
       	  z-shift  
        followed by the  
       	  pitch (rotation around x-axis in degrees)  
       	  roll  (rotation around y-axis in degrees)  
       	  yaw   (rotation around z-axis in degrees)  
        followed by the  
          x-rescaling factor  
          y-rescaling factor  
       	  z-rescaling factor  
         
        The order in which the transformations would be done is exactly opposite  
        as the list above, i.e. first z-rescale ... and finally x-shift.  
         
        Example use:  
          t0 = [1 2 3]; r0 = [10 20 30]; s0 = [1.1 1.2 1.3]  
          H0 = translate(t0) * rotate(r0) * scale(s0)  
          f = homogenous2traditional(H0)  
          t1 = f(1:3); r1 = f(4:6); s1 = f(7:9);  
          H1 = translate(t1) * rotate(r1) * scale(s1)  
         
        See also TRANSLATE, ROTATE, SCALE, HOMOGENOUS2QUATERNION, QUATERNION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/homogenous2traditional.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("homogenous2traditional", *args, **kwargs)
