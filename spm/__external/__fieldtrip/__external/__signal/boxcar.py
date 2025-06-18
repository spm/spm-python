from mpython import Runtime


def boxcar(*args, **kwargs):
    """
      BOXCAR returns a boxcar taper

        Use as
          w = boxcar(n)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/external/signal/boxcar.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("boxcar", *args, **kwargs)
