from spm._runtime import Runtime


def _mesh_octahedron(*args, **kwargs):
    r"""
      MESH_OCTAHEDRON returns the vertices and triangles of an octahedron  
         
        Use as  
          [pos tri] = mesh_octahedron;  
         
        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/utilities/private/mesh_octahedron.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_octahedron", *args, **kwargs)
