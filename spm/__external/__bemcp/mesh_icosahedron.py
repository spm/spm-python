from spm._runtime import Runtime


def mesh_icosahedron(*args, **kwargs):
    r"""
      MESH_ICOSAHEDRON returns the vertices and triangle of a 12-vertex icosahedral  
        mesh.  
         
        Use as  
          [pos, tri] = mesh_icosahedron  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/bemcp/mesh_icosahedron.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_icosahedron", *args, **kwargs)
