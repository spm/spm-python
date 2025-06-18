from mpython import Runtime


def _inside_contour(*args, **kwargs):
    """
    inside_contour is a function.
          bool = inside_contour(pos, contour)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/plotting/private/inside_contour.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("inside_contour", *args, **kwargs)
