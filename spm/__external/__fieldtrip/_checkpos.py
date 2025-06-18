from mpython import Runtime


def _checkpos(*args, **kwargs):
    """
      last input is always the required string


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/checkpos.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("checkpos", *args, **kwargs)
