from mpython import Runtime


def _vline(*args, **kwargs):
    """
      VLINE plot a vertical line in the current graph


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/vline.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("vline", *args, **kwargs, nargout=0)
