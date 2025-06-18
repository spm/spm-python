from mpython import Runtime


def _fixneighbours(*args, **kwargs):
    """
      This function converts the old format of the neighbourstructure into the
        new format - although it just works as a wrapper

        See also FT_NEIGHBOURSELECTION


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/fixneighbours.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixneighbours", *args, **kwargs)
