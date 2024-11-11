from spm.__wrapper__ import Runtime


def _mesh_tetrahedron(*args, **kwargs):
    """
      MESH_TETRAHEDRON returns the vertices and triangles of a tetrahedron.  
         
        Use as  
          [pos, tri] = mesh_tetrahedron;  
         
        See also MESH_ICOSAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mesh_tetrahedron.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mesh_tetrahedron", *args, **kwargs)
