from mpython import Runtime


def _ctranspose2x2(*args, **kwargs):
    """
      compute ctranspose of multiple 2x2 matrices, input is 2x2xN


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/connectivity/private/ctranspose2x2.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("ctranspose2x2", *args, **kwargs)
