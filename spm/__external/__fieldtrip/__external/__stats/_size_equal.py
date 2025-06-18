from mpython import Runtime


def _size_equal(*args, **kwargs):
    """
      returns true if all input arguments are equal to each other


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/stats/private/size_equal.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("size_equal", *args, **kwargs)
