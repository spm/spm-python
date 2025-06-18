from mpython import Runtime


def _cornerpoints(*args, **kwargs):
    """
      CORNERPOINTS returns the eight corner points of an anatomical volume
        in voxel and in head coordinates

        Use as
          [voxel, head] = cornerpoints(dim, transform)
        which will return two 8x3 matrices.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/cornerpoints.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("cornerpoints", *args, **kwargs)
