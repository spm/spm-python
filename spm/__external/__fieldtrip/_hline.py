from mpython import Runtime


def _hline(*args, **kwargs):
    """
      HLINE plot a horizontal line in the current graph


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/hline.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("hline", *args, **kwargs, nargout=0)
