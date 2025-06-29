from spm._runtime import Runtime


def _mesh_icosahedron(*args, **kwargs):
    """
      MESH_ICOSAHEDRON returns the vertices and triangle of a 12-vertex icosahedral  
        mesh.  
         
        Use as  
          [pos, tri] = mesh_icosahedron  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/mesh_icosahedron.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_icosahedron", *args, **kwargs)
