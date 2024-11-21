from spm.__wrapper__ import Runtime


def _mesh_cone(*args, **kwargs):
    """
      MESH_CONE creates a triangulated cone  
         
        Use as  
          [pnt, tri] = mesh_cone(N)  
         
        This creates a cone with N-2 vertices on the bottom circle and N vertices in total.  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON, MESH_SPHERE, MESH_CUBE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/mesh_cone.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mesh_cone", *args, **kwargs)
