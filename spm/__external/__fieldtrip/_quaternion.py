from spm.__wrapper__ import Runtime


def _quaternion(*args, **kwargs):
    """
      QUATERNION returns the homogenous coordinate transformation matrix corresponding to  
        a coordinate transformation described by 7 quaternion parameters.  
         
        Use as  
          [H] = quaternion(Q)  
        where  
          Q       [q0, q1, q2, q3, q4, q5, q6] vector with parameters  
          H       corresponding homogenous transformation matrix  
         
        If the input vector has length 6, it is assumed to represent a unit quaternion without scaling.  
         
        See Neuromag/Elekta/Megin MaxFilter manual version 2.2, section "D2 Coordinate Matching", page 77 for more details and  
        https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation#Conversion_to_and_from_the_matrix_representation  
         
        See also TRANSLATE, ROTATE, SCALE, HOMOGENOUS2QUATERNION  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/quaternion.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("quaternion", *args, **kwargs)
