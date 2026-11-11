from spm._runtime import Runtime


def _mesh_cube(*args, **kwargs):
    r"""
      MESH_CUBE creates a triangulated cube  
         
        Use as  
          [pos, tri] = mesh_cube()  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_ICOSAHEDRON, MESH_SPHERE, MESH_CONE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/plotting/private/mesh_cube.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_cube", *args, **kwargs)
