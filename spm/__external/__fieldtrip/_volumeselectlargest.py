from mpython import Runtime


def _volumeselectlargest(*args, **kwargs):
    """
      VOLUMESELECTLARGEST is a helper function for segmentations

        See also VOLUMEFILLHOLES, VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumeselectlargest.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumeselectlargest", *args, **kwargs)
