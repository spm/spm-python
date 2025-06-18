from mpython import Runtime


def bf_sources(*args, **kwargs):
    """
      Prepare source locations and lead fields for beamforming
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_sources.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_sources", *args, **kwargs)
