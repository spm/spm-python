from spm._runtime import Runtime


def _elec1020_follow(*args, **kwargs):
    """
      ELEC1020_FOLLOW  
      

    [Matlab code]( https://github.com/spm/spm/blob/main/external/fieldtrip/private/elec1020_follow.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("elec1020_follow", *args, **kwargs)
