from mpython import Runtime


def ltrisect(*args, **kwargs):
    """
      LTRISECT intersects a line with a plane spanned by three vertices

        Use as
          [sect] = ltrisect(v1, v2, v3, l1, l2)
        where v1, v2 and v3 are three vertices spanning the plane, and l1 and l2
        are two points on the line


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/src/ltrisect.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ltrisect", *args, **kwargs)
