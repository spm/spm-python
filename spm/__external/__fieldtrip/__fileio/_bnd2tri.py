from mpython import Runtime


def _bnd2tri(*args, **kwargs):
    """
      BND2TRI takes a struct array with one triangulated surface mesh per
        tissue and converts it into a single triangulated surface mesh
        represented as one long list of triangles with per triangle a tissue or
        region type.

        Use as
          [pos, tri, tissue] = bnd2tri(bnd)

        See also MESH2EDGE, POLY2TRI, TRI2BND


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/bnd2tri.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bnd2tri", *args, **kwargs)
