from mpython import Runtime


def _fixvolume(*args, **kwargs):
    """
      FIXVOLUME cleans up the volume data representation, removes old and obsoleted
        fields and ensures that it is consistent with the most recent code.

        Use as
          output = fixvolume(input)
        where input is a structure representing volume data

        See also FT_CHECKDATA, FIXSOURCE


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/utilities/private/fixvolume.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("fixvolume", *args, **kwargs)
