from mpython import Runtime


def _guidelines(*args, **kwargs):
    """
      GUIDELINES searches for a contiguous block of commented text and shows
        its contents. It is used to display additional help sections.


    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/guidelines.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("guidelines", *args, **kwargs)
