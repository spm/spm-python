from mpython import Runtime


def _volumepermute(*args, **kwargs):
    """
      VOLUMEPERMUTE

        See also VOLUMEFLIP, ALIGN_IJK2XYZ, ALIGN_XYZ2IJK


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/volumepermute.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("volumepermute", *args, **kwargs)
