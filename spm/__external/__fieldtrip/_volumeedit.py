from mpython import Runtime


def _volumeedit(*args, **kwargs):
    """
      VOLUMEEDIT allows for editing of a (booleanized) volume, in order to
        remove unwanted voxels. Interaction proceeds with the keyboard and the
        mouse.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumeedit.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumeedit", *args, **kwargs)
