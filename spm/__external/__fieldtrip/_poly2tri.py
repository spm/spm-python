from spm._runtime import Runtime


def _poly2tri(*args, **kwargs):
    r"""
      POLY2TRI converts the polygons in a mesh to triangles by splitting  
        them in half. The input polygons should consist of 4 vertices.  
        Curvature is not considered and the resulting split will only be  
        optimal for flat polygons.  
         
        Use as  
         mesh = poly2tri(mesh)  
         
        See also MESH2EDGE, TRI2BND  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/private/poly2tri.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("poly2tri", *args, **kwargs)
