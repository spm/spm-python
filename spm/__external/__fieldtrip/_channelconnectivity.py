from mpython import Runtime


def _channelconnectivity(*args, **kwargs):
    """
      CHANNELCONNECTIVIY creates a NxN matrix that describes whether channels
        are connected as neighbours

        See also FT_PREPARE_NEIGHBOURS, TRIANGLE2CONNECTIVITY


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/channelconnectivity.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("channelconnectivity", *args, **kwargs)
