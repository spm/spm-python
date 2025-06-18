from mpython import Runtime


def _mesh_spherify(*args, **kwargs):
    """
      Takes a cortical mesh and scales it so that it fits into a
        unit sphere.

        This function determines the points of the original mesh that support a
        convex hull and determines the radius of those points. Subsequently the
        radius of the support points is interpolated onto all vertices of the
        original mesh, and the vertices of the original mesh are scaled by
        dividing them by this interpolated radius.

        Use as
          [pnt, tri] = mesh_spherify(pnt, tri, ...)

        Optional arguments should come as key-value pairs and may include
          shift  = 'no', mean', 'range'
          smooth = number (default = 20)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/mesh_spherify.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("mesh_spherify", *args, **kwargs)
