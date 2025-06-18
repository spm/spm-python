from mpython import Runtime


def _routlm(*args, **kwargs):
    """
      ROUTLM computes the projection of a point from its la/mu parameters
        these equal the "Barycentric" coordinates

        Use as
          [proj] = routlm(v1, v2, v3, la, mu)
        where v1, v2 and v3 are three vertices of the triangle


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/routlm.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("routlm", *args, **kwargs)
