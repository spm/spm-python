from mpython import Runtime


def bf_view(*args, **kwargs):
    """
      Display the results of beamforming analysis
       __________________________________________________________________________


    [Matlab code]( https://github.com/spm/spm/blob/main/toolbox/DAiSS/bf_view.m )

    Copyright (C) 1995-2025 Functional Imaging Laboratory, Department of Imaging Neuroscience, UCL
    """

    return Runtime.call("bf_view", *args, **kwargs)
