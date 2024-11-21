from spm.__wrapper__ import Runtime


def _intersect_plane(*args, **kwargs):
    """
      INTERSECT_PLANE intersection between a triangulated surface mesh and a plane. It  
        returns the coordinates of the begin- and endpoints of the line segments that  
        together form the contour of the intersection.  
         
        Use as  
          [X, Y, Z] = intersect_plane(pos, tri, v1, v2, v3)  
         
        where the intersecting plane is spanned by the vertices v1, v2, v3 and the return  
        values are the X, Y and Z coordinates of the begin- and endpoints for all line  
        segments.  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/intersect_plane.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("intersect_plane", *args, **kwargs)
