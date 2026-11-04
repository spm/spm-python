from spm._runtime import Runtime


def _mesh_tetrahedron(*args, **kwargs):
    r"""
      MESH_TETRAHEDRON returns the vertices and triangles of a tetrahedron.  
         
        Use as  
          [pos, tri] = mesh_tetrahedron;  
         
        See also MESH_ICOSAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE  
      

    Generated from SPM26.10.01.

    [Source Matlab code]( https://github.com/spm/spm/blob/26.10.01/external/fieldtrip/forward/private/mesh_tetrahedron.m )

    Copyright (C) 1995-2026 Functional Imaging Laboratory, 
    Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_tetrahedron", *args, **kwargs)
