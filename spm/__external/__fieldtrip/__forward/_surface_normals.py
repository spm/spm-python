from mpython import Runtime


def _surface_normals(*args, **kwargs):
    """
      SURFACE_NORMALS compute the surface normals of a triangular mesh
        for each triangle or for each vertex

        Use as
          nrm = surface_normals(pnt, tri, opt)
        where opt is either 'vertex' (default) or 'triangle'.

        See also SURFACE_AREA, SURFACE_ORIENTATION, SURFACE_INSIDE, SURFACE_NESTING, PROJECTTRI, PCNORMALS


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/forward/private/surface_normals.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("surface_normals", *args, **kwargs)
