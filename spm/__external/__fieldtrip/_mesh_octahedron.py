from mpython import Runtime


def _mesh_octahedron(*args, **kwargs):
    """
      MESH_OCTAHEDRON returns the vertices and triangles of an octahedron

        Use as
          [pos tri] = mesh_octahedron;

        See also MESH_TETRAHEDRON, MESH_OCTAHEDRON, MESH_SPHERE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mesh_octahedron.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_octahedron", *args, **kwargs)
