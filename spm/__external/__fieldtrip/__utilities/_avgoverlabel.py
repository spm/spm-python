from mpython import Runtime


def _avgoverlabel(*args, **kwargs):
    """
    avgoverlabel is a function.
          str = avgoverlabel(label)


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/avgoverlabel.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("avgoverlabel", *args, **kwargs)
