from mpython import Runtime


def _GALA_calculate_distance(*args, **kwargs):
    """
    GALA_calculate_distance is a function.
          distance = GALA_calculate_distance(mesh)


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/private/GALA_calculate_distance.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("GALA_calculate_distance", *args, **kwargs)
