from spm.__wrapper__ import Runtime


def _mesh_cube(*args, **kwargs):
    """
      MESH_CUBE creates a triangulated cube  
         
        Use as  
          [pos, tri] = mesh_cube()  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON, MESH_SPHERE, MESH_CONE  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/mesh_cube.m )

    Copyright (C) 2024-2024 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """
    return Runtime.call("mesh_cube", *args, **kwargs)
