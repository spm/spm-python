from spm._runtime import Runtime


def _mesh_cone(*args, **kwargs):
    r"""
      MESH_CONE creates a triangulated cone  
         
        Use as  
          [pnt, tri] = mesh_cone(N)  
         
        This creates a cone with N-2 vertices on the bottom circle and N vertices in total.  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON, MESH_SPHERE, MESH_CUBE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/mesh_cone.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_cone", *args, **kwargs)
