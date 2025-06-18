from mpython import Runtime


def _tri2bnd(*args, **kwargs):
    """
      TRI2BND takes a triangulated surface mesh that is represented as one
        long list of triangles with per triangle a tissue or region type, and
        converts it in a struct array with one surface mesh per tissue.

        Use as
          [bnd, bndtissue] = tri2bnd(pos, tri, tritissue)

        The output "bnd" is a structure array with the fields bnd.pos and bnd.tri.

        See also MESH2EDGE, POLY2TRI, BND2TRI


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/fileio/private/tri2bnd.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("tri2bnd", *args, **kwargs)
