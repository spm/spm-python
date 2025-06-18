from mpython import Runtime


def _volumefillholes(*args, **kwargs):
    """
      VOLUMEFILLHOLES is a helper function for segmentations

        See also VOLUMETHRESHOLD, VOLUMESMOOTH, VOLUMEPAD, VOLUMESELECTLARGEST


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/volumefillholes.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumefillholes", *args, **kwargs)
