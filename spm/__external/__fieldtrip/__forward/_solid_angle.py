from spm.__wrapper__ import Runtime


def _solid_angle(*args, **kwargs):
    """
      SOLID_ANGLE of a planar triangle as seen from the origin  
         
        The solid angle W subtended by a surface S is defined as the surface  
        area W of a unit sphere covered by the surface's projection onto the  
        sphere. Solid angle is measured in steradians, and the solid angle  
        corresponding to all of space being subtended is 4*pi sterradians.  
         
        Use:  
          [w] = solid_angle(v1, v2, v3)  
        or  
          [w] = solid_angle(pnt, tri)  
        where v1, v2 and v3 are the vertices of a single triangle in 3D or  
        pnt and tri contain a description of a triangular mesh (this will  
        compute the solid angle for each triangle)  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/solid_angle.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("solid_angle", *args, **kwargs)
