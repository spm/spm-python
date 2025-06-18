from mpython import Runtime


def _undobalancing(*args, **kwargs):
    """
      UNDOBALANCING removes all balancing coefficients from the gradiometer sensor array

        This is used in CHANNELPOSITION, FT_PREPARE_LAYOUT, FT_SENSTYPE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/undobalancing.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("undobalancing", *args, **kwargs)
